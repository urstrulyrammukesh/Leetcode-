"""LeetCode 22. Generate Parentheses (Medium)
Approach: backtracking. Add '(' while some are left, and ')' only when it would not close more than opened.
Time O(4^n / sqrt(n)), space O(n) besides the output.
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(cur, opened, closed):
            if len(cur) == 2 * n:
                res.append(cur)
                return
            if opened < n:
                backtrack(cur + "(", opened + 1, closed)
            if closed < opened:
                backtrack(cur + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert s.generateParenthesis(1) == ["()"]
    print("lc22 ok")
