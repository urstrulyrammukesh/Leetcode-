"""LeetCode 876. Middle of the Linked List (Easy)
Approach: Slow moves one step, fast moves two; when fast ends, slow is in the middle.
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow


if __name__ == "__main__":
    s = Solution()
    assert to_list(s.middleNode(build([1, 2, 3, 4, 5]))) == [3, 4, 5]
    assert to_list(s.middleNode(build([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]
    print("lc876 ok")
