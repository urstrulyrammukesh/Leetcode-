"""LeetCode 295. Find Median from Data Stream (Hard)
Approach: two heaps. A max-heap keeps the smaller half and a min-heap the larger half, balanced in size.
Time O(log n) per add, O(1) per median; space O(n).
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.low = []   # max-heap (stored negated)
        self.high = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    for x in (-5, 10, 4):
        mf.addNum(x)
    assert mf.findMedian() == 2.5
    print("lc295 ok")
