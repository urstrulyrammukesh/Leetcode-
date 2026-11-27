"""LeetCode 103. Binary Tree Zigzag Level Order Traversal (Medium)
Approach: Normal BFS by levels; reverse every second level.
Time O(n), space O(n).
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        out, level = [], [root] if root else []
        while level:
            vals = [n.val for n in level]
            out.append(vals if len(out) % 2 == 0 else vals[::-1])
            level = [c for n in level for c in (n.left, n.right) if c]
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.zigzagLevelOrder(build([3, 9, 20, None, None, 15, 7])) == [[3], [20, 9], [15, 7]]
    assert s.zigzagLevelOrder(build([])) == []
    print("lc103 ok")
