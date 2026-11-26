"""LeetCode 141. Linked List Cycle (Easy)
Approach: Floyd's tortoise and hare. A fast pointer catches the slow one only if there is a loop.
Time O(n), space O(1).
"""
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val, self.next = x, None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


def build_with_cycle(vals, pos):
    nodes = [ListNode(v) for v in vals]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None


if __name__ == "__main__":
    s = Solution()
    assert s.hasCycle(build_with_cycle([3, 2, 0, -4], 1))
    assert s.hasCycle(build_with_cycle([1, 2], 0))
    assert not s.hasCycle(build_with_cycle([1], -1))
    print("lc141 ok")
