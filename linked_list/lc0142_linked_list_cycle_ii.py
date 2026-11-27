"""LeetCode 142. Linked List Cycle II (Medium)
Approach: Floyd: after slow and fast meet, a pointer from the head and one from the meeting point meet at the cycle start.
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
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                while head is not slow:
                    head, slow = head.next, slow.next
                return head
        return None


if __name__ == "__main__":
    s = Solution()
    h = build([3, 2, 0, -4])
    h.next.next.next.next = h.next
    assert s.detectCycle(h) is h.next
    assert s.detectCycle(build([1])) is None
    print("lc142 ok")
