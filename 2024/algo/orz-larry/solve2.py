import sys

MOD = int(1e9 + 9)


def solve(arr):
    dp = 256 * [0]

    for c in arr:
        dp[ord(c)] = (sum(dp) + 1) % MOD

    return (sum(dp) + 1) % MOD


for _ in range(int(input())):
    print(solve(input()))

print(input(), file=sys.stderr)
