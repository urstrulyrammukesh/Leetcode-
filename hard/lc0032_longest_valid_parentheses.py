"""LeetCode 32. Longest Valid Parentheses (Hard)
Approach: stack of indices; the bottom of the stack marks the last position a valid run could not cross.
Time O(n), space O(n).
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        best = 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    best = max(best, i - stack[-1])
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.longestValidParentheses("(()") == 2
    assert s.longestValidParentheses(")()())") == 4
    assert s.longestValidParentheses("") == 0
    assert s.longestValidParentheses("()(())") == 6
    print("lc32 ok")
