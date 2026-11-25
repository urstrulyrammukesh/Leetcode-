"""Reverse Linked List: reverse a singly linked list in place. O(n) time, O(1) space."""

class Node:
    def __init__(self, val, nxt=None):
        self.val, self.next = val, nxt

def reverse(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev

def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    head = Node(1, Node(2, Node(3, Node(4))))
    assert to_list(reverse(head)) == [4, 3, 2, 1]
    assert reverse(None) is None
    print("p03 ok")
