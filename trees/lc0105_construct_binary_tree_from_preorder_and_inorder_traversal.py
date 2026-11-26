"""LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal (Medium)
Approach: the next preorder value is the root; its position in inorder splits the left and right subtrees.
Time O(n) with a value-to-index map, space O(n).
"""
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        index = {v: i for i, v in enumerate(inorder)}
        pre = iter(preorder)

        def helper(lo, hi):
            if lo > hi:
                return None
            val = next(pre)
            node = TreeNode(val)
            mid = index[val]
            node.left = helper(lo, mid - 1)
            node.right = helper(mid + 1, hi)
            return node

        return helper(0, len(inorder) - 1)


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
    assert level_order(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])) == [3, 9, 20, None, None, 15, 7]
    assert level_order(s.buildTree([-1], [-1])) == [-1]
    print("lc105 ok")
