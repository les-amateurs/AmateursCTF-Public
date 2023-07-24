use crate::Graph;
use rand::prelude::*;
use std::iter;

/// Generates a valid [`Graph`] with 1412 nodes
pub fn gen_graph() -> Graph {
    const N: usize = 1412;

    let mut rng = thread_rng();

    // rough idea: we have some large SCCs of fixed size and a bunch of small SCCs
    // the large SCCs ensure the time complexity is about right
    // the large amount of small SCCs serve as basically a lot of small tests to ensure correctness
    // hopefully this makes it somewhat difficult to cheese
    let comp_sizes = {
        let mut comp_sizes = vec![1, 4, 1, 2, 14, 41, 12, 141, 412];
        let mut nodes_left = N - comp_sizes.iter().sum::<usize>();

        while nodes_left > 30 {
            let s = rng.gen_range(10..=30);
            comp_sizes.push(s);
            nodes_left -= s;
        }

        if nodes_left > 0 {
            comp_sizes.push(nodes_left);
        }

        assert_eq!(comp_sizes.iter().sum::<usize>(), N);

        // shuffle order of SCCs
        comp_sizes.shuffle(&mut rng);

        comp_sizes
    };

    let mut scc_comp = vec![0; N];
    {
        let mut u = 0;
        for (i, &x) in comp_sizes.iter().enumerate() {
            scc_comp[u..u + x].fill(i);
            u += x;
        }
        assert_eq!(u, N);
    }

    let mut graph = vec![vec![false; N]; N];

    for i in 0..N {
        // try to make the SCC a bit better than just completely random
        let p = rng.gen_range(0.1..0.9);

        for j in i + 1..N {
            if scc_comp[i] != scc_comp[j] {
                graph[i][j] = true;
                continue;
            }
            if rng.gen_bool(p) {
                graph[i][j] = true;
            } else {
                graph[j][i] = true;
            }
        }
    }

    // shuffle the vertices of the graph
    let perm = {
        let mut perm = (0..N).collect::<Vec<_>>();
        perm.shuffle(&mut rng);
        perm
    };
    let mut new_graph = vec![vec![false; N]; N];
    for i in 0..N {
        for j in 0..N {
            new_graph[perm[i]][perm[j]] = graph[i][j];
        }
    }

    // dbg!(scc_decomp(&Graph::new(new_graph.clone()))
    //     .iter()
    //     .map(|c| c.len())
    //     .collect::<Vec<_>>());

    Graph::new(new_graph)
}

/// Compute the SCCs of the graph, in topological order
fn scc_decomp(g: &Graph) -> Vec<Vec<usize>> {
    fn dfs<I: IntoIterator<Item = usize>>(
        g: &mut impl FnMut(usize) -> I,
        u: usize,
        vis: &mut [bool],
        ord: &mut Vec<usize>,
    ) {
        if vis[u] {
            return;
        }
        vis[u] = true;

        for v in g(u) {
            dfs(g, v, vis, ord);
        }

        ord.push(u);
    }

    let n = g.n();

    let ord = {
        let mut vis = vec![false; n];
        let mut ord = vec![];

        for i in 0..n {
            dfs(
                &mut |u| (0..n).filter(move |&v| g.has_road(u, v)),
                i,
                &mut vis,
                &mut ord,
            );
        }

        ord.reverse();
        ord
    };

    let mut comps = vec![];

    {
        let mut vis = vec![false; n];

        for &i in &ord {
            if vis[i] {
                continue;
            }

            let mut buf = vec![];
            dfs(
                &mut |u| (0..n).filter(move |&v| g.has_road(v, u)),
                i,
                &mut vis,
                &mut buf,
            );
            comps.push(buf);
        }
    }

    comps
}

/// All paths consist of multiple hamiltonian cycles in SCCs chained together.
/// Computes these chained hamiltonian cycles for nodes [u, n).
fn solve(g: &Graph, u: usize) -> Vec<Vec<usize>> {
    if u == g.n() - 1 {
        return vec![vec![u]];
    }

    let mut comps = solve(g, u + 1);

    let to_comp = comps
        .iter()
        .map(|c| c.iter().copied().find(|&v| g.has_road(u, v)))
        .collect::<Vec<_>>();
    let from_comp = comps
        .iter()
        .map(|c| c.iter().copied().find(|&v| g.has_road(v, u)))
        .collect::<Vec<_>>();

    let Some(first_to) = to_comp.iter().enumerate().filter_map(|(i, x)| x.and(Some(i))).min() else {
        // I point to nothing, so everything points to me
        comps.push(vec![u]);
        return comps;
    };
    let Some(last_from) = from_comp.iter().enumerate().filter_map(|(i, x)| x.and(Some(i))).max() else {
        // nothing points to me, so I point to everything
        comps.insert(0, vec![u]);
        return comps;
    };

    if first_to > last_from {
        // I'm a new SCC
        assert_eq!(last_from + 1, first_to);
        comps.insert(first_to, vec![u]);
        return comps;
    }

    if first_to == last_from {
        // add myself to an existing scc
        // something points to me in this SCC and I point to something,
        // so by IVT there must exist an adjacent pair where I can insert myself
        let scc = &mut comps[first_to];
        for i in 0..scc.len() {
            if g.has_road(scc[i], u) && g.has_road(u, scc[(i + 1) % scc.len()]) {
                scc.insert(i + 1, u);
                return comps;
            }
        }
        unreachable!();
    }

    assert!(first_to < last_from);
    // we merge SCCs together

    /// Rotate `arr` so `x` is the first element
    fn rotate(arr: &mut [usize], x: usize) {
        arr.rotate_left(arr.iter().position(|&y| x == y).unwrap());
    }

    // make sure u -> first element of first_to
    rotate(&mut comps[first_to], to_comp[first_to].unwrap());
    // make sure last element of last_from -> u
    rotate(&mut comps[last_from], from_comp[last_from].unwrap());
    comps[last_from].rotate_left(1);

    let new_comp = comps
        .drain(first_to..=last_from)
        .flatten()
        .chain(iter::once(u))
        .collect::<Vec<_>>();
    comps.insert(first_to, new_comp);

    comps
}

/// Requests help from the omniscient Warry to compute the optimal pilgrimages.
/// The `u`-th returned pilgrimage is the optimal one starting from statue `u`.
pub fn find_pilgrimages(g: &Graph) -> Vec<Vec<usize>> {
    let n = g.n();

    let ans = solve(g, 0);

    // do some sanity checking

    let sccs = scc_decomp(g);

    // each element of ans should be a permutation of the corresponding SCC
    {
        assert_eq!(ans.len(), sccs.len());

        let mut ans_ind = vec![None; n];
        let mut scc_ind = vec![None; n];

        for (i, c) in ans.iter().enumerate() {
            for &j in c {
                ans_ind[j] = Some(i);
            }
        }
        for (i, c) in sccs.iter().enumerate() {
            for &j in c {
                scc_ind[j] = Some(i);
            }
        }

        assert_eq!(ans_ind, scc_ind);
    }

    // each element of ans should be a valid pilgrimage
    {
        for c in &ans {
            g.assert_valid_pilgrimage(c);
        }
    }

    let mut p_ans = vec![vec![]; n];

    {
        let mut suff = vec![];

        for mut c in ans.into_iter().rev() {
            for _ in 0..c.len() {
                p_ans[c[0]].extend_from_slice(&c);
                p_ans[c[0]].extend_from_slice(&suff);

                c.rotate_left(1);
            }

            suff.splice(0..0, c);
        }
    }

    // check each pilgrimage really is optimal
    {
        let mut opt_ans = 0;

        for c in sccs.iter().rev() {
            opt_ans += c.len();
            for &i in c {
                assert_eq!(p_ans[i].len(), opt_ans);
            }
        }
    }

    // sanity check each pilgrimage is valid
    for c in &p_ans {
        g.assert_valid_pilgrimage(c);
    }

    p_ans
}
