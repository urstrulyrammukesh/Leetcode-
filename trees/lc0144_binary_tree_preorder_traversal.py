"""LeetCode 144. Binary Tree Preorder Traversal (Easy)
Approach: Iterative with a stack: visit the node, push right then left.
Time O(n), space O(height).
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        out, stack = [], [root] if root else []
        while stack:
            node = stack.pop()
            out.append(node.val)
            stack += [c for c in (node.right, node.left) if c]
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.preorderTraversal(build([1, None, 2, 3])) == [1, 2, 3]
    assert s.preorderTraversal(build([1, 2, 3, 4, 5])) == [1, 2, 4, 5, 3]
    print("lc144 ok")
