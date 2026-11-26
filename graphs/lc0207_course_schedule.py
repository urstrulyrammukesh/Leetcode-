"""LeetCode 207. Course Schedule (Medium)
Approach: Kahn's topological sort. If every course can be taken once its prerequisites are done, there is no cycle.
Time O(V + E), space O(V + E).
"""
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque(i for i in range(numCourses) if indegree[i] == 0)
        taken = 0
        while queue:
            c = queue.popleft()
            taken += 1
            for nxt in graph[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
        return taken == numCourses


if __name__ == "__main__":
    s = Solution()
    assert s.canFinish(2, [[1, 0]])
    assert not s.canFinish(2, [[1, 0], [0, 1]])
    print("lc207 ok")
