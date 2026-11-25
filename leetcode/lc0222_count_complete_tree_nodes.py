"""LeetCode 222. Count Complete Tree Nodes. If left and right heights match, the subtree is perfect: 2^h - 1 nodes. O(log^2 n) time."""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh, rh = 0, 0
        l, r = root, root
        while l:
            lh += 1
            l = l.left
        while r:
            rh += 1
            r = r.right
        if lh == rh:
            return (1 << lh) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

if __name__ == "__main__":
    T = TreeNode
    root = T(1, T(2, T(4), T(5)), T(3, T(6)))
    assert Solution().countNodes(root) == 6
    assert Solution().countNodes(None) == 0
    print("lc222 ok")
