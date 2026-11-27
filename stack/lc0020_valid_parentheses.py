"""LeetCode 20. Valid Parentheses (Easy)
Approach: Push opening brackets; every closing bracket must match the top of the stack.
Time O(n), space O(n).
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pair, stack = {")": "(", "]": "[", "}": "{"}, []
        for c in s:
            if c in pair:
                if not stack or stack.pop() != pair[c]:
                    return False
            else:
                stack.append(c)
        return not stack


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()[]{}")
    assert not s.isValid("(]")
    assert s.isValid("{[]}")
    assert not s.isValid("(")
    print("lc20 ok")
