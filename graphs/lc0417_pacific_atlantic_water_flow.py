"""LeetCode 417. Pacific Atlantic Water Flow (Medium)
Approach: Flood uphill from each ocean's edge; cells reached from both oceans are the answer.
Time O(m * n), space O(m * n).
"""


class Solution:
    def pacificAtlantic(self, h: list[list[int]]) -> list[list[int]]:
        R, C = len(h), len(h[0])

        def reach(starts):
            seen, stack = set(starts), list(starts)
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen and h[nr][nc] >= h[r][c]:
                        seen.add((nr, nc))
                        stack.append((nr, nc))
            return seen

        pac = reach([(0, c) for c in range(C)] + [(r, 0) for r in range(R)])
        atl = reach([(R - 1, c) for c in range(C)] + [(r, C - 1) for r in range(R)])
        return sorted([r, c] for r, c in pac & atl)


if __name__ == "__main__":
    s = Solution()
    h = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    assert s.pacificAtlantic(h) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert s.pacificAtlantic([[1]]) == [[0, 0]]
    print("lc417 ok")
