"""LeetCode 200. Number of Islands (Medium)
Approach: For each unvisited land cell, flood-fill its island and count one.
Time O(m * n), space O(m * n).
"""


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        R, C, count = len(grid), len(grid[0]), 0
        for r0 in range(R):
            for c0 in range(C):
                if grid[r0][c0] != "1":
                    continue
                count += 1
                stack = [(r0, c0)]
                while stack:
                    r, c = stack.pop()
                    if 0 <= r < R and 0 <= c < C and grid[r][c] == "1":
                        grid[r][c] = "0"
                        stack += [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        return count


if __name__ == "__main__":
    s = Solution()
    g = [list("11110"), list("11010"), list("11000"), list("00000")]
    assert s.numIslands(g) == 1
    g = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert s.numIslands(g) == 3
    print("lc200 ok")
