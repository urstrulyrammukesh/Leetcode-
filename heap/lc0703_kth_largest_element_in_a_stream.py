"""LeetCode 703. Kth Largest Element in a Stream (Easy)
Approach: A min-heap of size k: the smallest of the k largest is the k-th largest.
Time O(log k) per add, space O(k).
"""
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k, self.heap = k, []
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


if __name__ == "__main__":
    k = KthLargest(3, [4, 5, 8, 2])
    assert [k.add(3), k.add(5), k.add(10), k.add(9), k.add(4)] == [4, 5, 5, 8, 8]
    print("lc703 ok")
