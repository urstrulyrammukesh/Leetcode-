"""LeetCode 121. Best Time to Buy and Sell Stock (Easy)
Approach: keep the lowest price seen so far; selling today earns price - lowest.
Time O(n), space O(1).
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = float("inf")
        best = 0
        for p in prices:
            lowest = min(lowest, p)
            best = max(best, p - lowest)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    print("lc121 ok")
