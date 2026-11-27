"""LeetCode 7. Reverse Integer (Medium)
Approach: Reverse the digits of |x|, restore the sign, and return 0 if it leaves the 32-bit range.
Time O(digits), space O(1).
"""


class Solution:
    def reverse(self, x: int) -> int:
        r = int(str(abs(x))[::-1]) * (1 if x >= 0 else -1)
        return r if -2 ** 31 <= r < 2 ** 31 else 0


if __name__ == "__main__":
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(1534236469) == 0
    print("lc7 ok")
