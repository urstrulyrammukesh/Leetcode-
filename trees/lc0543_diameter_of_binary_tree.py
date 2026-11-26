"""LeetCode 543. Diameter of Binary Tree (Easy)
Approach: DFS returns each height; the longest path through a node is left height + right height.
Time O(n), space O(height).
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best = 0

        def height(node):
            nonlocal best
            if not node:
                return 0
            l, r = height(node.left), height(node.right)
            best = max(best, l + r)
            return 1 + max(l, r)

        height(root)
        return best


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
    assert s.diameterOfBinaryTree(build([1, 2, 3, 4, 5])) == 3
    assert s.diameterOfBinaryTree(build([1, 2])) == 1
    print("lc543 ok")
