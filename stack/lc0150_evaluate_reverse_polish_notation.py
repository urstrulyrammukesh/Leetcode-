"""LeetCode 150. Evaluate Reverse Polish Notation (Medium)
Approach: push numbers on a stack; an operator pops two, applies itself, and pushes the result.
Division truncates toward zero. Time O(n), space O(n).
"""


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for tok in tokens:
            if tok in "+-*/":
                b, a = stack.pop(), stack.pop()
                if tok == "+":
                    stack.append(a + b)
                elif tok == "-":
                    stack.append(a - b)
                elif tok == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(tok))
        return stack[0]


if __name__ == "__main__":
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    print("lc150 ok")
