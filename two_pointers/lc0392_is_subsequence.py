"""LeetCode 392. Is Subsequence (Easy)
Approach: Walk t once and advance a pointer in s on every match.
Time O(len t), space O(1).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for c in t:
            if i < len(s) and s[i] == c:
                i += 1
        return i == len(s)


if __name__ == "__main__":
    s = Solution()
    assert s.isSubsequence("abc", "ahbgdc")
    assert not s.isSubsequence("axc", "ahbgdc")
    assert s.isSubsequence("", "abc")
    print("lc392 ok")
