"""LeetCode 1971. Find if Path Exists in Graph (Easy)
Approach: Union-find over the edges, then check whether source and destination share a root.
Time O(E * a(n)), space O(n).
"""


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            parent[find(a)] = find(b)
        return find(source) == find(destination)


if __name__ == "__main__":
    s = Solution()
    assert s.validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2)
    assert not s.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5)
    print("lc1971 ok")
