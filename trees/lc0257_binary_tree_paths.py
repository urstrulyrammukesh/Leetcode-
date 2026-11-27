"""LeetCode 257. Binary Tree Paths (Easy)
Approach: DFS carrying the path so far as text; save it at every leaf.
Time O(n * h), space O(n * h).
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> list[str]:
        out = []

        def dfs(node, path):
            if not node:
                return
            path = f"{path}->{node.val}" if path else str(node.val)
            if not node.left and not node.right:
                out.append(path)
            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.binaryTreePaths(build([1, 2, 3, None, 5])) == ["1->2->5", "1->3"]
    assert s.binaryTreePaths(build([1])) == ["1"]
    print("lc257 ok")
