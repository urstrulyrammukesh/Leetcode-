"""LeetCode 153. Find Minimum in Rotated Sorted Array (Medium)
Approach: binary search against the right end; if mid is bigger than the right end, the minimum is to the right.
Time O(log n), space O(1).
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
    print("lc153 ok")
