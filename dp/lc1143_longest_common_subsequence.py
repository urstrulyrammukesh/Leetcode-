"""LeetCode 1143. Longest Common Subsequence (Medium)
Approach: 2-D DP. Matching characters extend the diagonal; otherwise take the better of skipping one side.
Time O(m * n), space O(n) with a rolling row.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        prev = [0] * (len(text2) + 1)
        for a in text1:
            cur = [0]
            for j, b in enumerate(text2):
                cur.append(prev[j] + 1 if a == b else max(prev[j + 1], cur[j]))
            prev = cur
        return prev[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonSubsequence("abcde", "ace") == 3
    assert s.longestCommonSubsequence("abc", "abc") == 3
    assert s.longestCommonSubsequence("abc", "def") == 0
    print("lc1143 ok")
