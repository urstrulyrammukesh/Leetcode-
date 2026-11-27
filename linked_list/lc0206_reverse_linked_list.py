"""LeetCode 206. Reverse Linked List (Easy)
Approach: Walk the list and point each node back at the previous one.
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.reverseList(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(s.reverseList(build([]))) == []
    print("lc206 ok")
