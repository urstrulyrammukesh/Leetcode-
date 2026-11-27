"""LeetCode 9. Palindrome Number (Easy)
Approach: Reverse only the second half of the digits and compare with the first half (no strings).
Time O(digits), space O(1).
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x):
            return False
        half = 0
        while x > half:
            x, half = x // 10, half * 10 + x % 10
        return x == half or x == half // 10


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121)
    assert not s.isPalindrome(-121)
    assert not s.isPalindrome(10)
    assert s.isPalindrome(0)
    print("lc9 ok")
