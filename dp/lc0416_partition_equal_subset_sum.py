"""LeetCode 416. Partition Equal Subset Sum (Medium)
Approach: 0/1 knapsack as a bitset: bit k is set when some subset sums to k; check half the total.
Time O(n * sum), space O(sum).
"""


class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        bits = 1
        for x in nums:
            bits |= bits << x
        return bool(bits >> (total // 2) & 1)


if __name__ == "__main__":
    s = Solution()
    assert s.canPartition([1, 5, 11, 5])
    assert not s.canPartition([1, 2, 3, 5])
    print("lc416 ok")
