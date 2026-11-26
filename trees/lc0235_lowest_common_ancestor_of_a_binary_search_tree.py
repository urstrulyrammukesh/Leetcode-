"""LeetCode 235. Lowest Common Ancestor of a Binary Search Tree (Medium)
Approach: walk down from the root; the first node that splits p and q (or equals one) is the answer.
Time O(height), space O(1).
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node


def find(root, val):
    while root and root.val != val:
        root = root.left if val < root.val else root.right
    return root


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


if __name__ == "__main__":
    s = Solution()
    root = build([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert s.lowestCommonAncestor(root, find(root, 2), find(root, 8)).val == 6
    assert s.lowestCommonAncestor(root, find(root, 2), find(root, 4)).val == 2
    assert s.lowestCommonAncestor(root, find(root, 3), find(root, 5)).val == 4
    print("lc235 ok")
