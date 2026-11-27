"""LeetCode 547. Number of Provinces (Medium)
Approach: Union-find over the adjacency matrix; count the distinct roots.
Time O(n^2 * a(n)), space O(n).
"""


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    parent[find(i)] = find(j)
        return len({find(i) for i in range(n)})


if __name__ == "__main__":
    s = Solution()
    assert s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    print("lc547 ok")
