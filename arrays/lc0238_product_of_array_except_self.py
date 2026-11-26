"""LeetCode 238. Product of Array Except Self (Medium)
Approach: prefix products from the left, then multiply by suffix products from the right, no division.
Time O(n), space O(1) extra besides the output.
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        out = [1] * n
        prefix = 1
        for i in range(n):
            out[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            out[i] *= suffix
            suffix *= nums[i]
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    print("lc238 ok")
