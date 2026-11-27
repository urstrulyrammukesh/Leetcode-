"""LeetCode 1584. Min Cost to Connect All Points (Medium)
Approach: Prim's algorithm on the complete graph with Manhattan distances (O(n^2), no heap needed).
Time O(n^2), space O(n).
"""


class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        best = [float("inf")] * n
        used = [False] * n
        best[0], total = 0, 0
        for _ in range(n):
            u = min((i for i in range(n) if not used[i]), key=best.__getitem__)
            used[u] = True
            total += best[u]
            for v in range(n):
                if not used[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    best[v] = min(best[v], d)
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
    print("lc1584 ok")
