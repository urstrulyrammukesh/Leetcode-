"""LeetCode 283. Move Zeroes (Easy)
Approach: a write pointer swaps every non-zero forward, so zeros drift to the end in place.
Time O(n), space O(1).
"""


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    Solution().moveZeroes(a)
    assert a == [1, 3, 12, 0, 0]
    b = [0]
    Solution().moveZeroes(b)
    assert b == [0]
    print("lc283 ok")
