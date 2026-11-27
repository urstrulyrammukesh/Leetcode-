"""LeetCode 494. Target Sum (Medium)
Approach: Count sign choices with a map from running sum to number of ways.
Time O(n * range of sums), space O(range of sums).
"""
from collections import Counter


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        ways = Counter({0: 1})
        for x in nums:
            nxt = Counter()
            for total, w in ways.items():
                nxt[total + x] += w
                nxt[total - x] += w
            ways = nxt
        return ways[target]


if __name__ == "__main__":
    s = Solution()
    assert s.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert s.findTargetSumWays([1], 1) == 1
    print("lc494 ok")
