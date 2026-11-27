"""LeetCode 64. Minimum Path Sum (Medium)
Approach: Each cell's best cost is its value plus the cheaper of the cells above and to the left.
Time O(m * n), space O(n).
"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [float("inf")] * len(grid[0])
        dp[0] = 0
        for row in grid:
            for j, x in enumerate(row):
                dp[j] = x + (min(dp[j], dp[j - 1]) if j else dp[j])
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert s.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
    print("lc64 ok")
