"""LeetCode 154. Find Minimum in Rotated Sorted Array II (Hard)
Approach: binary search against the right end; when nums[mid] == nums[hi] we cannot tell, so shrink hi by one.
Time O(log n) on average, O(n) worst case with many duplicates; space O(1).
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1
        return nums[lo]


if __name__ == "__main__":
    s = Solution()
    assert s.findMin([1, 3, 5]) == 1
    assert s.findMin([2, 2, 2, 0, 1]) == 0
    assert s.findMin([3, 1, 3]) == 1
    assert s.findMin([10, 1, 10, 10, 10]) == 1
    print("lc154 ok")
