# standard LIS...
# but did you realize negative indices exist??

import random
from bisect import bisect_left


def gen(n_min, n_max):
    n = random.randint(n_min, n_max)
    ans = []
    for _ in range(n):
        ans.append(random.randint(1, int(1e9)))
    return ans


def solve_lis(arr):
    f = [-1]
    f_from = [-1]
    dp_from = []
    for i, x in enumerate(arr):
        ind = bisect_left(f, x)
        dp_from.append(f_from[ind - 1])
        if ind == len(f):
            f.append(0)
            f_from.append(0)
        f[ind] = x
        f_from[ind] = i

    ans = []
    i = f_from[-1]
    while i != -1:
        ans.append(i)
        i = dp_from[i]
    ans.reverse()
    return ans


def solve(arr):
    ans = solve_lis(2 * arr)
    for i in range(len(ans)):
        ans[i] -= len(arr)
    return ans
