"""LeetCode 44. Wildcard Matching (Hard)
Approach: DP. '*' either matches nothing (move in p) or one more char (move in s).
Time O(m * n), space O(m * n).
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        for j in range(n - 1, -1, -1):
            dp[m][j] = p[j] == "*" and dp[m][j + 1]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if p[j] == "*":
                    dp[i][j] = dp[i][j + 1] or dp[i + 1][j]
                else:
                    dp[i][j] = p[j] in (s[i], "?") and dp[i + 1][j + 1]
        return dp[0][0]


if __name__ == "__main__":
    s = Solution()
    assert not s.isMatch("aa", "a")
    assert s.isMatch("aa", "*")
    assert not s.isMatch("cb", "?a")
    assert s.isMatch("adceb", "*a*b")
    assert not s.isMatch("acdcb", "a*c?b")
    assert s.isMatch("", "***")
    print("lc44 ok")
