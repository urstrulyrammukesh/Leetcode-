"""LeetCode 10. Regular Expression Matching (Hard)
Approach: bottom-up DP. dp[i][j] is True when s[i:] matches p[j:]; a '*' either skips "x*" or eats one char.
Time O(m * n), space O(m * n).
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                first = i < m and p[j] in (s[i], ".")
                if j + 1 < n and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (first and dp[i + 1][j])
                else:
                    dp[i][j] = first and dp[i + 1][j + 1]
        return dp[0][0]


if __name__ == "__main__":
    s = Solution()
    assert not s.isMatch("aa", "a")
    assert s.isMatch("aa", "a*")
    assert s.isMatch("ab", ".*")
    assert s.isMatch("aab", "c*a*b")
    assert not s.isMatch("mississippi", "mis*is*p*.")
    print("lc10 ok")
