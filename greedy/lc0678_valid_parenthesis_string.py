"""LeetCode 678. Valid Parenthesis String (Medium)
Approach: Track the lowest and highest possible number of open brackets; '*' widens the range.
Time O(n), space O(1).
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            lo += 1 if c == "(" else -1
            hi += 1 if c != ")" else -1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0


if __name__ == "__main__":
    s = Solution()
    assert s.checkValidString("()")
    assert s.checkValidString("(*)")
    assert s.checkValidString("(*))")
    assert not s.checkValidString(")(")
    print("lc678 ok")
