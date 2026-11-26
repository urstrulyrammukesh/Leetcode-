"""LeetCode 188. Best Time to Buy and Sell Stock IV (Hard)
Approach: DP over transactions. buy[t] / sell[t] are the best profits holding / not holding after the t-th buy.
Time O(n * k), space O(k).
"""
from math import inf


class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        if not prices or k == 0:
            return 0
        buy = [-inf] * (k + 1)
        sell = [0] * (k + 1)
        for p in prices:
            for t in range(1, k + 1):
                buy[t] = max(buy[t], sell[t - 1] - p)
                sell[t] = max(sell[t], buy[t] + p)
        return sell[k]


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit(2, [2, 4, 1]) == 2
    assert s.maxProfit(2, [3, 2, 6, 5, 0, 3]) == 7
    assert s.maxProfit(1, [7, 6, 4, 3, 1]) == 0
    print("lc188 ok")
