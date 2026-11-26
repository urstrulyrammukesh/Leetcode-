"""LeetCode 198. House Robber (Medium)
Approach: DP. At each house, either skip it or rob it plus the best from two houses back.
Time O(n), space O(1).
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = prev1 = 0
        for x in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + x)
        return prev1


if __name__ == "__main__":
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
    print("lc198 ok")
