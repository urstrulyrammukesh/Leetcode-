"""LeetCode 152. Maximum Product Subarray (Medium)
Approach: Track both the largest and smallest product ending here, since a negative number swaps them.
Time O(n), space O(1).
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        best = hi = lo = nums[0]
        for x in nums[1:]:
            hi, lo = max(x, hi * x, lo * x), min(x, hi * x, lo * x)
            best = max(best, hi)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxProduct([2, 3, -2, 4]) == 6
    assert s.maxProduct([-2, 0, -1]) == 0
    assert s.maxProduct([-2, 3, -4]) == 24
    print("lc152 ok")
