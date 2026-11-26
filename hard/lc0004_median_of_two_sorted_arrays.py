"""LeetCode 4. Median of Two Sorted Arrays (Hard)
Approach: binary search a partition of the shorter array so the left halves hold the smaller half of all numbers.
Time O(log(min(m, n))), space O(1).
"""
from math import inf


class Solution:
    def findMedianSortedArrays(self, a: list[int], b: list[int]) -> float:
        if len(a) > len(b):
            a, b = b, a
        m, n = len(a), len(b)
        half = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            al = a[i - 1] if i > 0 else -inf
            ar = a[i] if i < m else inf
            bl = b[j - 1] if j > 0 else -inf
            br = b[j] if j < n else inf
            if al <= br and bl <= ar:
                if (m + n) % 2:
                    return float(max(al, bl))
                return (max(al, bl) + min(ar, br)) / 2
            if al > br:
                hi = i - 1
            else:
                lo = i + 1
        raise ValueError("inputs must be sorted")


if __name__ == "__main__":
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([], [1]) == 1.0
    assert s.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    print("lc4 ok")
