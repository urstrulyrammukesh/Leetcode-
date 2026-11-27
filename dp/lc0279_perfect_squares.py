"""LeetCode 279. Perfect Squares (Medium)
Approach: dp[n] = 1 + min(dp[n - k^2]) over all squares k^2 <= n.
Time O(n * sqrt n), space O(n).
"""


class Solution:
    def numSquares(self, n: int) -> int:
        squares = [k * k for k in range(1, int(n ** 0.5) + 1)]
        dp = [0] + [n] * n
        for i in range(1, n + 1):
            dp[i] = 1 + min(dp[i - q] for q in squares if q <= i)
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    assert s.numSquares(12) == 3
    assert s.numSquares(13) == 2
    assert s.numSquares(1) == 1
    print("lc279 ok")
