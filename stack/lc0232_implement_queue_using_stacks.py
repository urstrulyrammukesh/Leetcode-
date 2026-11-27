"""LeetCode 232. Implement Queue using Stacks (Easy)
Approach: Push onto an in-stack; when popping, refill the out-stack only when it is empty (amortised O(1)).
Amortised O(1) per operation.
"""


class MyQueue:
    def __init__(self):
        self.inbox, self.outbox = [], []

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def _move(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def pop(self) -> int:
        self._move()
        return self.outbox.pop()

    def peek(self) -> int:
        self._move()
        return self.outbox[-1]

    def empty(self) -> bool:
        return not self.inbox and not self.outbox


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1 and q.pop() == 1 and not q.empty()
    q.push(3)
    assert q.pop() == 2 and q.pop() == 3 and q.empty()
    print("lc232 ok")
