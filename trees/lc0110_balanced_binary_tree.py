"""LeetCode 110. Balanced Binary Tree (Easy)
Approach: DFS returns the height, or -1 as soon as any subtree is unbalanced.
Time O(n), space O(height).
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            l, r = height(node.left), height(node.right)
            if l < 0 or r < 0 or abs(l - r) > 1:
                return -1
            return 1 + max(l, r)

        return height(root) >= 0


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
    assert s.isBalanced(build([3, 9, 20, None, None, 15, 7]))
    assert not s.isBalanced(build([1, 2, 2, 3, 3, None, None, 4, 4]))
    assert s.isBalanced(build([]))
    print("lc110 ok")
