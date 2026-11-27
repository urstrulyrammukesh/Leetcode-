"""LeetCode 268. Missing Number (Easy)
Approach: The sum 0..n minus the sum of the array is the missing number.
Time O(n), space O(1).
"""


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    s = Solution()
    assert s.missingNumber([3, 0, 1]) == 2
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    print("lc268 ok")
