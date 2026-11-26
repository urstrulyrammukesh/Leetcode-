"""LeetCode 125. Valid Palindrome (Easy)
Approach: two pointers from both ends, skipping anything that is not a letter or digit.
Time O(n), space O(1).
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama")
    assert not s.isPalindrome("race a car")
    assert s.isPalindrome(" ")
    print("lc125 ok")
