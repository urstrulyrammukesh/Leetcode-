"""LeetCode 69. Sqrt(x). Binary search on the answer, no built-in power functions. O(log x) time, O(1) space."""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right, ans = 1, x // 2, 0
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid <= x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

if __name__ == "__main__":
    s = Solution()
    assert [s.mySqrt(x) for x in (0, 1, 4, 8, 16, 2147395599)] == [0, 1, 2, 2, 4, 46339]
    print("lc69 ok")
