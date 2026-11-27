"""LeetCode 96. Unique Binary Search Trees (Medium)
Approach: Catalan numbers: pick each value as root, multiply the counts of left and right subtrees.
Time O(n^2), space O(n).
"""


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] * (n + 1)
        for k in range(2, n + 1):
            dp[k] = sum(dp[r] * dp[k - 1 - r] for r in range(k))
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    assert s.numTrees(3) == 5
    assert s.numTrees(1) == 1
    assert s.numTrees(19) == 1767263190
    print("lc96 ok")
