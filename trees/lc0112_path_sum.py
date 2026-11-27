"""LeetCode 112. Path Sum (Easy)
Approach: Subtract each value on the way down; at a leaf the remainder must be zero.
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
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == target
        rest = target - root.val
        return self.hasPathSum(root.left, rest) or self.hasPathSum(root.right, rest)


if __name__ == "__main__":
    s = Solution()
    assert s.hasPathSum(build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22)
    assert not s.hasPathSum(build([1, 2, 3]), 5)
    assert not s.hasPathSum(build([]), 0)
    print("lc112 ok")
