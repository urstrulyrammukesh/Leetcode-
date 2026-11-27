"""LeetCode 160. Intersection of Two Linked Lists (Easy)
Approach: Two pointers that switch to the other list at the end meet at the intersection (or both reach None).
Time O(m + n), space O(1).
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
    def getIntersectionNode(self, a: ListNode, b: ListNode) -> Optional[ListNode]:
        p, q = a, b
        while p is not q:
            p = p.next if p else b
            q = q.next if q else a
        return p


if __name__ == "__main__":
    s = Solution()
    common = build([8, 4, 5])
    a, b = build([4, 1]), build([5, 6, 1])
    a.next.next = common
    b.next.next.next = common
    assert s.getIntersectionNode(a, b) is common
    assert s.getIntersectionNode(build([2, 6, 4]), build([1, 5])) is None
    print("lc160 ok")
