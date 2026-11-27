"""LeetCode 61. Rotate List (Medium)
Approach: Make the list a ring, then cut it len - k % len steps from the old head.
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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n, tail = 1, head
        while tail.next:
            tail, n = tail.next, n + 1
        tail.next = head
        for _ in range(n - k % n):
            tail = tail.next
        head, tail.next = tail.next, None
        return head


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.rotateRight(build([1, 2, 3, 4, 5]), 2)) == [4, 5, 1, 2, 3]
    assert to_list(s.rotateRight(build([0, 1, 2]), 4)) == [2, 0, 1]
    assert to_list(s.rotateRight(build([]), 1)) == []
    print("lc61 ok")
