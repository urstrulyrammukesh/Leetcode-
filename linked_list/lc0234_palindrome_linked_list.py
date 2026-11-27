"""LeetCode 234. Palindrome Linked List (Easy)
Approach: Find the middle with slow/fast pointers, reverse the second half, compare both halves.
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        while prev:
            if prev.val != head.val:
                return False
            prev, head = prev.next, head.next
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(build([1, 2, 2, 1]))
    assert not s.isPalindrome(build([1, 2]))
    assert s.isPalindrome(build([1, 2, 3, 2, 1]))
    print("lc234 ok")
