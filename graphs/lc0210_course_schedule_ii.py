"""LeetCode 210. Course Schedule II (Medium)
Approach: Kahn's topological sort, recording the order courses are taken; empty if there is a cycle.
Time O(V + E), space O(V + E).
"""
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        order = []
        while queue:
            c = queue.popleft()
            order.append(c)
            for nxt in graph[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return order if len(order) == numCourses else []


if __name__ == "__main__":
    s = Solution()
    prereqs = [[1, 0], [2, 0], [3, 1], [3, 2]]
    order = s.findOrder(4, prereqs)
    pos = {c: i for i, c in enumerate(order)}
    assert sorted(order) == [0, 1, 2, 3] and all(pos[pre] < pos[c] for c, pre in prereqs)
    assert s.findOrder(2, [[1, 0], [0, 1]]) == []
    assert s.findOrder(1, []) == [0]
    print("lc210 ok")
