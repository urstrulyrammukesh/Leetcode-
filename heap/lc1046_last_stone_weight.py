"""LeetCode 1046. Last Stone Weight (Easy)
Approach: Max-heap (negated values): smash the two heaviest and push back the difference.
Time O(n log n), space O(n).
"""
import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            a, b = -heapq.heappop(heap), -heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, b - a)
        return -heap[0] if heap else 0


if __name__ == "__main__":
    s = Solution()
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([1]) == 1
    assert s.lastStoneWeight([2, 2]) == 0
    print("lc1046 ok")
