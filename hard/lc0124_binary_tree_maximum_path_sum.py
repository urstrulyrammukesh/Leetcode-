"""LeetCode 124. Binary Tree Maximum Path Sum (Hard)
Approach: post-order DFS. Each node returns its best single downward branch; the answer may bend through the node.
Time O(n), space O(height).
"""
from collections import deque
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -inf

        def gain(node):
            nonlocal best
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return best


def build(vals):
    """Build a tree from LeetCode's level-order list, e.g. [1, None, 2]."""
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


if __name__ == "__main__":
    s = Solution()
    assert s.maxPathSum(build([1, 2, 3])) == 6
    assert s.maxPathSum(build([-10, 9, 20, None, None, 15, 7])) == 42
    assert s.maxPathSum(build([-3])) == -3
    print("lc124 ok")
