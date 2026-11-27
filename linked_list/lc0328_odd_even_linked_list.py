"""LeetCode 328. Odd Even Linked List (Medium)
Approach: Build the odd and even chains in one pass, then attach the even chain after the odd one.
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd, even, even_head = head, head.next, head.next
        while even and even.next:
            odd.next = odd = even.next
            even.next = even = odd.next
        odd.next = even_head
        return head


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.oddEvenList(build([1, 2, 3, 4, 5]))) == [1, 3, 5, 2, 4]
    assert to_list(s.oddEvenList(build([2, 1, 3, 5, 6, 4, 7]))) == [2, 3, 6, 7, 1, 5, 4]
    print("lc328 ok")
