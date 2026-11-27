"""LeetCode 680. Valid Palindrome II (Easy)
Approach: Two pointers; on the first mismatch try skipping either the left or the right character.
Time O(n), space O(1).
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def pal(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i, j = i + 1, j - 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return pal(i + 1, j) or pal(i, j - 1)
            i, j = i + 1, j - 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.validPalindrome("aba")
    assert s.validPalindrome("abca")
    assert not s.validPalindrome("abc")
    print("lc680 ok")
