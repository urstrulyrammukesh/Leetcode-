"""LeetCode 50. Pow(x, n) (Medium)
Approach: Fast exponentiation by squaring; a negative n means 1 / x^-n.
Time O(log n), space O(1).
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        out = 1.0
        while n:
            if n & 1:
                out *= x
            x *= x
            n >>= 1
        return out


if __name__ == "__main__":
    s = Solution()
    assert abs(s.myPow(2.0, 10) - 1024.0) < 1e-9
    assert abs(s.myPow(2.1, 3) - 9.261) < 1e-9
    assert abs(s.myPow(2.0, -2) - 0.25) < 1e-9
    print("lc50 ok")
