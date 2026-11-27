"""LeetCode 435. Non-overlapping Intervals (Medium)
Approach: Greedy: sort by end and keep every interval that starts after the last kept end; the rest must go.
Time O(n log n), space O(1) extra.
"""


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        removed, end = 0, float("-inf")
        for a, b in sorted(intervals, key=lambda x: x[1]):
            if a >= end:
                end = b
            else:
                removed += 1
        return removed


if __name__ == "__main__":
    s = Solution()
    assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
    print("lc435 ok")
