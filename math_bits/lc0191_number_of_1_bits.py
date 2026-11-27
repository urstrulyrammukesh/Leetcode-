"""LeetCode 191. Number of 1 Bits (Easy)
Approach: n & (n - 1) clears the lowest set bit; count how many times until zero.
Time O(set bits), space O(1).
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.hammingWeight(11) == 3
    assert s.hammingWeight(128) == 1
    assert s.hammingWeight(2147483645) == 30
    print("lc191 ok")
