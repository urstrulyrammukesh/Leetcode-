"""LeetCode 24. Swap Nodes in Pairs (Medium)
Approach: Use a dummy head and rewire each pair: prev -> b -> a -> rest.
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(0, head)
        while prev.next and prev.next.next:
            a, b = prev.next, prev.next.next
            prev.next, a.next, b.next = b, b.next, a
            prev = a
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.swapPairs(build([1, 2, 3, 4]))) == [2, 1, 4, 3]
    assert to_list(s.swapPairs(build([1, 2, 3]))) == [2, 1, 3]
    assert to_list(s.swapPairs(build([]))) == []
    print("lc24 ok")
