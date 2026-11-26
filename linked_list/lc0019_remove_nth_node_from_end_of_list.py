"""LeetCode 19. Remove Nth Node From End of List (Medium)
Approach: move a fast pointer n steps ahead, then move both; when fast ends, slow sits before the node to remove.
Time O(n), one pass; space O(1).
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next


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


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.removeNthFromEnd(build([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]
    assert to_list(s.removeNthFromEnd(build([1]), 1)) == []
    assert to_list(s.removeNthFromEnd(build([1, 2]), 1)) == [1]
    print("lc19 ok")
