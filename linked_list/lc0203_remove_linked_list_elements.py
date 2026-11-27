"""LeetCode 203. Remove Linked List Elements (Easy)
Approach: Dummy head so the first node can be removed like any other.
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = cur = ListNode(0, head)
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.removeElements(build([1, 2, 6, 3, 4, 5, 6]), 6)) == [1, 2, 3, 4, 5]
    assert to_list(s.removeElements(build([7, 7, 7, 7]), 7)) == []
    print("lc203 ok")
