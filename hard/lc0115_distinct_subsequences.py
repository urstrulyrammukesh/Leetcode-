"""LeetCode 115. Distinct Subsequences (Hard)
Approach: 1-D DP. dp[j] counts ways to form t[:j]; walk j backwards so each character of s is used once.
Time O(|s| * |t|), space O(|t|).
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] + [0] * len(t)
        for ch in s:
            for j in range(len(t) - 1, -1, -1):
                if t[j] == ch:
                    dp[j + 1] += dp[j]
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.numDistinct("rabbbit", "rabbit") == 3
    assert s.numDistinct("babgbag", "bag") == 5
    assert s.numDistinct("abc", "") == 1
    print("lc115 ok")
