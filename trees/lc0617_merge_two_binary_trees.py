"""LeetCode 617. Merge Two Binary Trees (Easy)
Approach: Recursively add overlapping nodes; where only one tree has a node, reuse it.
Time O(min(m, n)), space O(height).
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
    def mergeTrees(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> Optional[TreeNode]:
        if not a or not b:
            return a or b
        return TreeNode(a.val + b.val, self.mergeTrees(a.left, b.left), self.mergeTrees(a.right, b.right))


if __name__ == "__main__":
    s = Solution()
    assert level_order(s.mergeTrees(build([1, 3, 2, 5]), build([2, 1, 3, None, 4, None, 7]))) == [3, 4, 5, 5, 4, None, 7]
    assert level_order(s.mergeTrees(build([1]), build([1, 2]))) == [2, 2]
    print("lc617 ok")
