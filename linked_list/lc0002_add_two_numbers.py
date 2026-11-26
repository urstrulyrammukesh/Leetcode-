"""LeetCode 2. Add Two Numbers (Medium)
Approach: add digit by digit like on paper, carrying into the next node.
Time O(max(m, n)), space O(1) extra besides the output.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next


class Solution:
    def addTwoNumbers(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode()
        carry = 0
        while a or b or carry:
            total = carry + (a.val if a else 0) + (b.val if b else 0)
            carry, digit = divmod(total, 10)
            tail.next = tail = ListNode(digit)
            a = a.next if a else None
            b = b.next if b else None
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
    assert to_list(s.addTwoNumbers(build([2, 4, 3]), build([5, 6, 4]))) == [7, 0, 8]
    assert to_list(s.addTwoNumbers(build([0]), build([0]))) == [0]
    assert to_list(s.addTwoNumbers(build([9] * 7), build([9] * 4))) == [8, 9, 9, 9, 0, 0, 0, 1]
    print("lc2 ok")
