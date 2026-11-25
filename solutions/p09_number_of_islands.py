"""Number of Islands: count groups of connected '1's in a grid (BFS). O(rows * cols)."""
from collections import deque

def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    seen, count = set(), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in seen:
                count += 1
                seen.add((r, c))
                q = deque([(r, c)])
                while q:
                    x, y = q.popleft()
                    for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1" and (nx, ny) not in seen:
                            seen.add((nx, ny))
                            q.append((nx, ny))
    return count

if __name__ == "__main__":
    grid = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(grid) == 3
    assert num_islands([list("000")]) == 0
    print("p09 ok")
