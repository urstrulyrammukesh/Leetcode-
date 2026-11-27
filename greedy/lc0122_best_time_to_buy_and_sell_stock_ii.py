"""LeetCode 122. Best Time to Buy and Sell Stock II (Medium)
Approach: Take every upward step: the sum of all positive day-to-day differences.
Time O(n), space O(1).
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(max(0, b - a) for a, b in zip(prices, prices[1:]))


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    print("lc122 ok")
