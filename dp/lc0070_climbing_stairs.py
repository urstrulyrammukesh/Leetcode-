"""LeetCode 70. Climbing Stairs (Easy)
Approach: Ways to reach step n = ways(n - 1) + ways(n - 2): Fibonacci with two variables.
Time O(n), space O(1).
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    s = Solution()
    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(10) == 89
    print("lc70 ok")
