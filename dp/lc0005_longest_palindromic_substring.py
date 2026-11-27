"""LeetCode 5. Longest Palindromic Substring (Medium)
Approach: Expand around every centre (one letter and between two letters) and keep the longest.
Time O(n^2), space O(1).
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        for c in range(len(s)):
            for lo, hi in ((c, c), (c, c + 1)):
                while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                    lo, hi = lo - 1, hi + 1
                if hi - lo - 1 > len(best):
                    best = s[lo + 1:hi]
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.longestPalindrome("babad") in ("bab", "aba")
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("a") == "a"
    print("lc5 ok")
