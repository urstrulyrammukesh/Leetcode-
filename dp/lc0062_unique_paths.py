"""LeetCode 62. Unique Paths (Medium)
Approach: DP row by row. Paths to a cell = paths from above + paths from the left.
Time O(m * n), space O(n).
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                row[j] += row[j - 1]
        return row[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.uniquePaths(3, 7) == 28
    assert s.uniquePaths(3, 2) == 3
    assert s.uniquePaths(1, 1) == 1
    print("lc62 ok")
