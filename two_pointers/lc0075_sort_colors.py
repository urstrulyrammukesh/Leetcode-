"""LeetCode 75. Sort Colors (Medium)
Approach: Dutch national flag. Three pointers keep 0s on the left, 2s on the right, 1s in the middle.
Time O(n), space O(1), one pass.
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
            else:
                mid += 1


if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(a)
    assert a == [0, 0, 1, 1, 2, 2]
    b = [2, 0, 1]
    Solution().sortColors(b)
    assert b == [0, 1, 2]
    print("lc75 ok")
