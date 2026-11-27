"""LeetCode 63. Unique Paths II (Medium)
Approach: One row of DP: paths into a cell = paths from above + from the left, zero on obstacles.
Time O(m * n), space O(n).
"""


class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:
        dp = [0] * len(grid[0])
        dp[0] = 1
        for row in grid:
            for j, cell in enumerate(row):
                if cell:
                    dp[j] = 0
                elif j:
                    dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert s.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
    assert s.uniquePathsWithObstacles([[1]]) == 0
    print("lc63 ok")
