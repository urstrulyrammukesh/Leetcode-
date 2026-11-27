"""LeetCode 367. Valid Perfect Square (Easy)
Approach: Binary search for an integer r with r * r == num, without using sqrt.
Time O(log n), space O(1).
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.isPerfectSquare(16)
    assert not s.isPerfectSquare(14)
    assert s.isPerfectSquare(1)
    print("lc367 ok")
