"""LeetCode 1448. Count Good Nodes in Binary Tree (Medium)
Approach: DFS carrying the largest value seen on the path; a node is good when it is at least that big.
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
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, best):
            if not node:
                return 0
            best = max(best, node.val)
            return (node.val >= best) + dfs(node.left, best) + dfs(node.right, best)

        return dfs(root, root.val)


if __name__ == "__main__":
    s = Solution()
    assert s.goodNodes(build([3, 1, 4, 3, None, 1, 5])) == 4
    assert s.goodNodes(build([3, 3, None, 4, 2])) == 3
    assert s.goodNodes(build([1])) == 1
    print("lc1448 ok")
