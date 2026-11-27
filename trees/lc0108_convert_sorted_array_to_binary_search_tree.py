"""LeetCode 108. Convert Sorted Array to Binary Search Tree (Easy)
Approach: The middle element becomes the root; build both halves the same way (height-balanced).
Time O(n), space O(log n).
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


# ---- helpers for local testing (LeetCode gives you TreeNode) ----
def build(vals):
    """Build a tree from LeetCode level-order form, e.g. [1, None, 2]."""
    if not vals or vals[0] is None:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    queue = deque([root])
    while queue:
        node = queue.popleft()
        for side in ("left", "right"):
            v = next(it, "end")
            if v == "end":
                return root
            if v is not None:
                child = TreeNode(v)
                setattr(node, side, child)
                queue.append(child)
    return root


def level_order(root):
    out, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        out.append(node.val if node else None)
        if node:
            queue.extend((node.left, node.right))
    while out and out[-1] is None:
        out.pop()
    return out


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def make(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            return TreeNode(nums[mid], make(lo, mid - 1), make(mid + 1, hi))

        return make(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()
    root = s.sortedArrayToBST([-10, -3, 0, 5, 9])

    def inorder(n):
        return inorder(n.left) + [n.val] + inorder(n.right) if n else []

    def height(n):
        return 1 + max(height(n.left), height(n.right)) if n else 0

    assert inorder(root) == [-10, -3, 0, 5, 9] and height(root) == 3
    print("lc108 ok")
