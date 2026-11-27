"""LeetCode 91. Decode Ways (Medium)
Approach: Ways to decode s[:i] = ways(i - 1) if the last digit is 1-9, plus ways(i - 2) if the last two form 10-26.
Time O(n), space O(1).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        prev, cur = 0, 1  # ways for s[:i-1], s[:i]
        for i, c in enumerate(s):
            nxt = cur if c != "0" else 0
            if i and 10 <= int(s[i - 1:i + 1]) <= 26:
                nxt += prev
            prev, cur = cur, nxt
        return cur


if __name__ == "__main__":
    s = Solution()
    assert s.numDecodings("12") == 2
    assert s.numDecodings("226") == 3
    assert s.numDecodings("06") == 0
    assert s.numDecodings("11106") == 2
    print("lc91 ok")
