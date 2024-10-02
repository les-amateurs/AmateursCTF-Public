//! # Solution
//!
//! Consider the substitution
//! - `l = 00`
//! - `o = 01`
//! - `z = 10`
//! - `y = 11`
//!
//! If we work backwards, we see that our expansions are effectively doing `ab bc -> ac`.
//!
//! Let's disregard the `00` and `11`s for now. The `01` and the `10`s can be arranged in either one or two ways
//! (depending on if the number of them are equal).
//! Finally, we insert the `00` and `11`s in between the gaps using stars and bars.

const MOD: u64 = super::MOD as u64;

fn pow(base: u32, mut exp: u64) -> u32 {
    let mut base = base as u64;
    let mut ans = 1;

    while exp > 0 {
        if exp & 1 == 1 {
            ans = (ans * base) % MOD;
        }
        base = (base * base) % MOD;
        exp >>= 1;
    }

    ans as u32
}

fn inv(x: u32) -> u32 {
    pow(x, MOD - 2)
}

struct Math {
    fact: Vec<u32>,
    ifact: Vec<u32>,
}

impl Math {
    fn new(n: usize) -> Self {
        let mut fact = vec![0; n + 1];
        let mut ifact = vec![0; n + 1];

        fact[0] = 1;
        ifact[0] = 1;

        for i in 1..=n {
            fact[i] = ((fact[i - 1] as u64 * i as u64) % MOD) as u32;
        }

        ifact[n] = inv(fact[n]);
        for i in (1..n).rev() {
            ifact[i] = ((ifact[i + 1] as u64 * (i + 1) as u64) % MOD) as u32;
        }

        Self { fact, ifact }
    }

    fn choose(&self, n: usize, k: usize) -> u32 {
        (self.fact[n] as u64 * self.ifact[k] as u64 % MOD * self.ifact[n - k] as u64 % MOD) as u32
    }
}

pub fn solve(s: &str) -> u32 {
    let math = Math::new(s.len() + 10);

    let mut counter = [0usize; 256];
    for &c in s.as_bytes() {
        counter[c as usize] += 1;
    }

    let (o, z, l, y) = (
        counter['o' as usize],
        counter['z' as usize],
        counter['l' as usize],
        counter['y' as usize],
    );

    if (o as isize - z as isize).abs() > 1 {
        return 0;
    }

    // insert k things into n gaps
    fn ways_insert(math: &Math, n: usize, k: usize) -> u64 {
        if n == 0 {
            if k > 0 {
                return 0;
            } else {
                return 1;
            }
        }

        math.choose(k + n - 1, k) as u64
    }

    (if o == z {
        (ways_insert(&math, o, l) * ways_insert(&math, o + 1, y)
            + ways_insert(&math, o + 1, l) * ways_insert(&math, o, y))
            % MOD
    } else {
        let n = o.max(z);

        ways_insert(&math, n, l) * ways_insert(&math, n, y) % MOD
    }) as u32
}
