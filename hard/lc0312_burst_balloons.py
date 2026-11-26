"""LeetCode 312. Burst Balloons (Hard)
Approach: interval DP. Choose k as the LAST balloon burst between l and r, so its neighbours are exactly a[l] and a[r].
Time O(n^3), space O(n^2).
"""


class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        a = [1] + nums + [1]
        n = len(a)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for l in range(n - length):
                r = l + length
                for k in range(l + 1, r):
                    dp[l][r] = max(dp[l][r], a[l] * a[k] * a[r] + dp[l][k] + dp[k][r])
        return dp[0][n - 1]


if __name__ == "__main__":
    s = Solution()
    assert s.maxCoins([3, 1, 5, 8]) == 167
    assert s.maxCoins([1, 5]) == 10
    assert s.maxCoins([]) == 0
    print("lc312 ok")
