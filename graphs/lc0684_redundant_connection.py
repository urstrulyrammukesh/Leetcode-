"""LeetCode 684. Redundant Connection (Medium)
Approach: Union-find: the first edge whose two ends already share a root closes the cycle.
Time O(n * a(n)), space O(n).
"""


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return [a, b]
            parent[ra] = rb
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    print("lc684 ok")
