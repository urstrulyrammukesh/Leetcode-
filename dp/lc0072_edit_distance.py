"""LeetCode 72. Edit Distance (Medium)
Approach: dp[i][j] = edits to turn word1[:i] into word2[:j]: keep on a match, else 1 + min(insert, delete, replace).
Time O(m * n), space O(n).
"""


class Solution:
    def minDistance(self, a: str, b: str) -> int:
        prev = list(range(len(b) + 1))
        for i in range(1, len(a) + 1):
            cur = [i] + [0] * len(b)
            for j in range(1, len(b) + 1):
                cur[j] = prev[j - 1] if a[i - 1] == b[j - 1] else 1 + min(prev[j], cur[j - 1], prev[j - 1])
            prev = cur
        return prev[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5
    assert s.minDistance("", "abc") == 3
    print("lc72 ok")
