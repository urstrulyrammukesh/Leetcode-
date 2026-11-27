"""LeetCode 120. Triangle (Medium)
Approach: Bottom-up: each cell becomes itself plus the smaller of the two cells below it.
Time O(n^2), space O(n).
"""


class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        dp = triangle[-1][:]
        for row in reversed(triangle[:-1]):
            dp = [x + min(dp[i], dp[i + 1]) for i, x in enumerate(row)]
        return dp[0]


if __name__ == "__main__":
    s = Solution()
    assert s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert s.minimumTotal([[-10]]) == -10
    print("lc120 ok")
