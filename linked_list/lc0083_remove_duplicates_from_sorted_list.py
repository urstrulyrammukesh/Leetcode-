"""LeetCode 83. Remove Duplicates from Sorted List (Easy)
Approach: Skip the next node while it holds the same value.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.deleteDuplicates(build([1, 1, 2]))) == [1, 2]
    assert to_list(s.deleteDuplicates(build([1, 1, 2, 3, 3]))) == [1, 2, 3]
    print("lc83 ok")
