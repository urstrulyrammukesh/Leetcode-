"""LeetCode 785. Is Graph Bipartite? (Medium)
Approach: Two-colour every component with BFS; an edge between equal colours means not bipartite.
Time O(V + E), space O(V).
"""


class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}
        for start in range(len(graph)):
            if start in color:
                continue
            color[start], stack = 0, [start]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if v not in color:
                        color[v] = 1 - color[u]
                        stack.append(v)
                    elif color[v] == color[u]:
                        return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert not s.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    assert s.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
    print("lc785 ok")
