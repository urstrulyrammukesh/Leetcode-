"""LeetCode 213. House Robber II (Medium)
Approach: houses form a circle, so the first and last cannot both be robbed: solve House Robber without the
first house and without the last, and take the better one.
Time O(n), space O(1).
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        def line(houses):
            prev2 = prev1 = 0
            for x in houses:
                prev2, prev1 = prev1, max(prev1, prev2 + x)
            return prev1

        if len(nums) == 1:
            return nums[0]
        return max(line(nums[1:]), line(nums[:-1]))


if __name__ == "__main__":
    s = Solution()
    assert s.rob([2, 3, 2]) == 3
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([1, 2, 3]) == 3
    assert s.rob([5]) == 5
    print("lc213 ok")
