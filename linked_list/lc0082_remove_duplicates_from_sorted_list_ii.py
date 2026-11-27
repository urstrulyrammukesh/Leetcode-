"""LeetCode 82. Remove Duplicates from Sorted List II (Medium)
Approach: Dummy head; when a run of equal values starts, skip the whole run.
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
        dummy = prev = ListNode(0, head)
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.deleteDuplicates(build([1, 2, 3, 3, 4, 4, 5]))) == [1, 2, 5]
    assert to_list(s.deleteDuplicates(build([1, 1, 1, 2, 3]))) == [2, 3]
    print("lc82 ok")
