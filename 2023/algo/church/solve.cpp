#include "bits/extc++.h"

using namespace std;

template <typename T, typename... U>
void dbgh(const T& t, const U&... u) {
    cerr << t;
    ((cerr << " | " << u), ...);
    cerr << endl;
}

#ifdef DEBUG
#define dbg(...)                                           \
    cerr << "L" << __LINE__ << " [" << #__VA_ARGS__ << "]" \
         << ": ";                                          \
    dbgh(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define endl "\n"
#define long int64_t
#define sz(x) int(std::size(x))

constexpr int maxn = 2005;

bool graph[maxn][maxn];

vector<vector<int>> solve(int ind) {
    if (!ind) {
        return {{0}};
    }
    auto comps = solve(ind - 1);
    pair<int, int> lopt {-1, -1}, fopt = {sz(comps), sz(comps)};
    for (int i = 0; i < sz(comps); i++) {
        for (auto& a : comps[i]) {
            if (graph[ind][a]) {
                fopt = min(fopt, {i, a});
            } else {
                lopt = max(lopt, {i, a});
            }
        }
    }
    int last_to = lopt.first, first_from = fopt.first;
    if (last_to + 1 == first_from) {
        comps.insert(comps.begin() + first_from, {ind});
        return comps;
    }
    vector<int> nv {ind};
    if (first_from == last_to) {
        auto& ccomp = comps[first_from];
        for (int i = 0, prv = ccomp.back(); i < sz(ccomp); i++) {
            if (graph[ind][ccomp[i]] && graph[prv][ind]) {
                rotate(begin(ccomp), ccomp.begin() + i, end(ccomp));
                nv.insert(nv.end(), begin(ccomp), end(ccomp));
                break;
            }
            prv = ccomp[i];
        }
    } else {
        rotate(
            comps[first_from].begin(),
            find(begin(comps[first_from]), end(comps[first_from]), fopt.second),
            comps[first_from].end());
        rotate(
            begin(comps[last_to]),
            find(begin(comps[last_to]), end(comps[last_to]), lopt.second) + 1,
            end(comps[last_to]));
        for (int i = first_from; i <= last_to; i++) {
            nv.insert(nv.end(), begin(comps[i]), end(comps[i]));
        }
    }
    comps.erase(comps.begin() + first_from, comps.begin() + last_to);
    comps[first_from] = nv;
    return comps;
}

void solve() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < n; j++) {
            graph[i][j] = s[j] == '1';
        }
    }
    auto comps = solve(n - 1);
    vector<int> ans[n], cans;
    for (int i = sz(comps) - 1; i >= 0; i--) {
        for (int j = 0; j < sz(comps[i]); j++) {
            ans[comps[i][0]] = comps[i];
            ans[comps[i][0]].insert(ans[comps[i][0]].end(), begin(cans),
                                    end(cans));
            rotate(comps[i].begin(), comps[i].begin() + 1, comps[i].end());
        }
        cans.insert(cans.begin(), begin(comps[i]), end(comps[i]));
    }
    for (auto& a : ans) {
        for (int i = 0; i < sz(a) - 1; i++) {
            assert(graph[a[i]][a[i + 1]]);
        }
        for (int i = 0; i < sz(a); i++) {
            cout << a[i] << " \n"[i == sz(a) - 1];
        }
    }

    string output;
    while (!sz(output)) {
        getline(cin, output);
    }
    cerr << output << endl;
}

int main() {
    cin.exceptions(ios::failbit);
    ios_base::sync_with_stdio(false);
    solve();
}
