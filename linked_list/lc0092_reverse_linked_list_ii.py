"""LeetCode 92. Reverse Linked List II (Medium)
Approach: Walk to the node before `left`, then move each next node to the front of the sublist (head insertion).
Time O(n), space O(1).
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


def build(vals):
    dummy = cur = ListNode()
    for v in vals:
        cur.next = cur = ListNode(v)
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next
        for _ in range(right - left):
            nxt = cur.next
            cur.next, nxt.next, prev.next = nxt.next, prev.next, nxt
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.reverseBetween(build([1, 2, 3, 4, 5]), 2, 4)) == [1, 4, 3, 2, 5]
    assert to_list(s.reverseBetween(build([5]), 1, 1)) == [5]
    print("lc92 ok")
