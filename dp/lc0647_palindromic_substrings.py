"""LeetCode 647. Palindromic Substrings (Medium)
Approach: Expand around every centre and count each palindrome found on the way out.
Time O(n^2), space O(1).
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for c in range(len(s)):
            for lo, hi in ((c, c), (c, c + 1)):
                while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                    count += 1
                    lo, hi = lo - 1, hi + 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.countSubstrings("abc") == 3
    assert s.countSubstrings("aaa") == 6
    print("lc647 ok")
