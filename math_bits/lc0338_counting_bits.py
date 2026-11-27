"""LeetCode 338. Counting Bits (Easy)
Approach: bits[i] = bits[i >> 1] + (i & 1): drop the last bit, then add it back.
Time O(n), space O(n).
"""


class Solution:
    def countBits(self, n: int) -> list[int]:
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits


if __name__ == "__main__":
    s = Solution()
    assert s.countBits(2) == [0, 1, 1]
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
    print("lc338 ok")
