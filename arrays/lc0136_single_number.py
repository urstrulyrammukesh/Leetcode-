"""LeetCode 136. Single Number (Easy)
Approach: XOR of all numbers: pairs cancel out (x ^ x = 0), only the single one is left.
Time O(n), space O(1).
"""
from functools import reduce
from operator import xor


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        return reduce(xor, nums, 0)


if __name__ == "__main__":
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1]) == 1
    print("lc136 ok")
