"""LeetCode 41. First Missing Positive (Hard)
Approach: cyclic sort. Put every value v in 1..n at index v-1, then the first index i with nums[i] != i+1 gives the answer.
Time O(n), space O(1).
"""


class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


if __name__ == "__main__":
    s = Solution()
    assert s.firstMissingPositive([1, 2, 0]) == 3
    assert s.firstMissingPositive([3, 4, -1, 1]) == 2
    assert s.firstMissingPositive([7, 8, 9, 11, 12]) == 1
    assert s.firstMissingPositive([1, 1]) == 2
    print("lc41 ok")
