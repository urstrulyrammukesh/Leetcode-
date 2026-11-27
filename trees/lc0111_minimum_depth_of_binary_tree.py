"""LeetCode 111. Minimum Depth of Binary Tree (Easy)
Approach: BFS: the first leaf reached gives the minimum depth.
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, d = queue.popleft()
            if not node.left and not node.right:
                return d
            for c in (node.left, node.right):
                if c:
                    queue.append((c, d + 1))


if __name__ == "__main__":
    s = Solution()
    assert s.minDepth(build([3, 9, 20, None, None, 15, 7])) == 2
    assert s.minDepth(build([2, None, 3, None, 4, None, 5, None, 6])) == 5
    assert s.minDepth(build([])) == 0
    print("lc111 ok")
