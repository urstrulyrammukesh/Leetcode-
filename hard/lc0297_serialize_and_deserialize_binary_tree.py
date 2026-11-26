"""LeetCode 297. Serialize and Deserialize Binary Tree (Hard)
Approach: pre-order traversal with '#' for empty children; rebuild by reading the same order back.
Time O(n), space O(n).
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val, self.left, self.right = x, None, None


class Codec:
    def serialize(self, root):
        out = []

        def pre(node):
            if not node:
                out.append("#")
                return
            out.append(str(node.val))
            pre(node.left)
            pre(node.right)

        pre(root)
        return ",".join(out)

    def deserialize(self, data):
        vals = iter(data.split(","))

        def build():
            v = next(vals)
            if v == "#":
                return None
            node = TreeNode(int(v))
            node.left = build()
            node.right = build()
            return node

        return build()


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
    root = TreeNode(1)
    root.left, root.right = TreeNode(2), TreeNode(3)
    root.right.left, root.right.right = TreeNode(4), TreeNode(-5)
    codec = Codec()
    data = codec.serialize(root)
    assert level_order(codec.deserialize(data)) == [1, 2, 3, None, None, 4, -5]
    assert codec.serialize(None) == "#"
    assert codec.deserialize("#") is None
    print("lc297 ok")
