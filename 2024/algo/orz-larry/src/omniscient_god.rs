//! # Solution
//! Let `dp(n, c)` denote the number of distinct subsequences of `s[0..n]` that end with character `c`
//!
//! Let `c = s[n]`. Now, let's compute `dp(n + 1, d)`. Obviously, if `c != d` `dp(n + 1, d) = dp(n, d)`.
//! Now, we deal with `dp(n + 1, c)`. For any subsequence `t` of `s[0..=n]` that ends in `c`, we have two cases:
//! - `t` is also a subsequence of `s[0..n]`: `dp(n, c)` counts this.
//! - `t` is not a subsequence of `s[0..n]`: in this case consider `t'`, which is `t` but with all trailing `c`'s trimmed.
//! Obviously, `t'` is a subsequence of `s[0..n]`, and `t` must be `t'` with as many `c`'s appended to the end of it as possible
//! (to make sure `t` is not a subsequence of `s[0..n]`). Thus, this case corresponds to the number of
//! subsequences of `s[0..n]` not ending in `c`.
//!
//! Adding the above two cases together gives us the transition of `dp(n + 1, c) = 1 + sum_i dp(n, i)`.

use super::MOD;

pub fn solve(s: &str) -> u32 {
    let arr = s.as_bytes();
    let mut dp = [0; 256];

    for &c in arr {
        let c = c as usize;

        dp[c] = (dp.iter().sum::<u64>() + 1) % MOD as u64;
    }

    ((dp.iter().sum::<u64>() + 1) % MOD as u64) as u32
}
