"""LeetCode 852. Peak Index in a Mountain Array (Medium)
Approach: Climb toward the bigger neighbour: if arr[mid] < arr[mid + 1] the peak is to the right.
Time O(log n), space O(1).
"""


class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        lo, hi = 0, len(arr) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if arr[mid] < arr[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.peakIndexInMountainArray([0, 1, 0]) == 1
    assert s.peakIndexInMountainArray([0, 2, 1, 0]) == 1
    assert s.peakIndexInMountainArray([0, 10, 5, 2]) == 1
    print("lc852 ok")
