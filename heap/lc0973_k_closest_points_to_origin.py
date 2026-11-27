"""LeetCode 973. K Closest Points to Origin (Medium)
Approach: heapq.nsmallest by squared distance (no square roots needed).
Time O(n log k), space O(k).
"""
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])


if __name__ == "__main__":
    s = Solution()
    assert s.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert sorted(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2)) == [[-2, 4], [3, 3]]
    print("lc973 ok")
