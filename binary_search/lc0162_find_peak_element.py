"""LeetCode 162. Find Peak Element (Medium)
Approach: If nums[mid] < nums[mid + 1] a peak lies to the right, otherwise at mid or to the left.
Time O(log n), space O(1).
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1
            else:
                hi = mid
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in (1, 5)
    assert s.findPeakElement([1]) == 0
    print("lc162 ok")
