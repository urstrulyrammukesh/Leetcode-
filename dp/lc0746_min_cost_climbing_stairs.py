"""LeetCode 746. Min Cost Climbing Stairs (Easy)
Approach: Cost to stand past step i = cost[i] + min of the two steps before.
Time O(n), space O(1).
"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a = b = 0
        for c in cost:
            a, b = b, c + min(a, b)
        return min(a, b)


if __name__ == "__main__":
    s = Solution()
    assert s.minCostClimbingStairs([10, 15, 20]) == 15
    assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    print("lc746 ok")
