"""LeetCode 518. Coin Change II (Medium)
Approach: Unbounded knapsack counting: loop over coins outside so each combination is counted once.
Time O(coins * amount), space O(amount).
"""


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [1] + [0] * amount
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]
        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    assert s.change(5, [1, 2, 5]) == 4
    assert s.change(3, [2]) == 0
    assert s.change(10, [10]) == 1
    print("lc518 ok")
