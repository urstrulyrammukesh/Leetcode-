"""LeetCode 329. Longest Increasing Path in a Matrix (Hard)
Approach: DFS with memoisation; the longest path starting at a cell never changes, so compute it once.
Time O(rows * cols), space O(rows * cols).
"""
from functools import lru_cache


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        @lru_cache(maxsize=None)
        def dfs(r, c):
            best = 1
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    best = max(best, 1 + dfs(nr, nc))
            return best

        return max(dfs(r, c) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    s = Solution()
    assert s.longestIncreasingPath([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert s.longestIncreasingPath([[3, 4, 5], [3, 2, 6], [2, 2, 1]]) == 4
    assert s.longestIncreasingPath([[1]]) == 1
    print("lc329 ok")
