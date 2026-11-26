"""LeetCode 155. Min Stack (Medium)
Approach: store (value, minimum so far) pairs so getMin is the top pair's second item.
Time O(1) for every operation, space O(n).
"""


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        current_min = min(val, self.stack[-1][1]) if self.stack else val
        self.stack.append((val, current_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


if __name__ == "__main__":
    st = MinStack()
    st.push(-2)
    st.push(0)
    st.push(-3)
    assert st.getMin() == -3
    st.pop()
    assert st.top() == 0
    assert st.getMin() == -2
    print("lc155 ok")
