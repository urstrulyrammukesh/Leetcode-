"""LeetCode 113. Path Sum II (Medium)
Approach: Backtracking DFS that keeps the current path and records it at leaves that hit the target.
Time O(n^2) worst case, space O(height).
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
    def pathSum(self, root: Optional[TreeNode], target: int) -> list[list[int]]:
        out, path = [], []

        def dfs(node, rest):
            if not node:
                return
            path.append(node.val)
            rest -= node.val
            if not node.left and not node.right and rest == 0:
                out.append(path[:])
            dfs(node.left, rest)
            dfs(node.right, rest)
            path.pop()

        dfs(root, target)
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.pathSum(build([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
    assert s.pathSum(build([1, 2]), 0) == []
    print("lc113 ok")
