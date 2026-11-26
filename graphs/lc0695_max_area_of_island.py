"""LeetCode 695. Max Area of Island (Medium)
Approach: DFS from every unvisited land cell, counting cells and sinking them so they are not counted twice.
Time O(rows * cols), space O(rows * cols).
"""


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        best = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                area, stack = 0, [(r, c)]
                grid[r][c] = 0
                while stack:
                    x, y = stack.pop()
                    area += 1
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                            grid[nx][ny] = 0
                            stack.append((nx, ny))
                best = max(best, area)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxAreaOfIsland([[1, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 1]]) == 5
    assert s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    assert s.maxAreaOfIsland([[1]]) == 1
    print("lc695 ok")
