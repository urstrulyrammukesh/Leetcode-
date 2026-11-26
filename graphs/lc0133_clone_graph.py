"""LeetCode 133. Clone Graph (Medium)
Approach: DFS with a map from each original node to its copy, so cycles are copied once.
Time O(V + E), space O(V).
"""
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        copies = {}

        def clone(n):
            if n in copies:
                return copies[n]
            copy = Node(n.val)
            copies[n] = copy
            copy.neighbors = [clone(nb) for nb in n.neighbors]
            return copy

        return clone(node) if node else None


def build(adj):
    nodes = [Node(i + 1) for i in range(len(adj))]
    for node, nbrs in zip(nodes, adj):
        node.neighbors = [nodes[j - 1] for j in nbrs]
    return nodes[0] if nodes else None


def to_adj(node):
    seen, stack = {}, [node]
    while stack:
        n = stack.pop()
        if n.val in seen:
            continue
        seen[n.val] = n
        stack.extend(n.neighbors)
    return [[nb.val for nb in seen[v].neighbors] for v in sorted(seen)], set(map(id, seen.values()))


if __name__ == "__main__":
    adj = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = build(adj)
    copy = Solution().cloneGraph(original)
    copy_adj, copy_ids = to_adj(copy)
    _, original_ids = to_adj(original)
    assert copy_adj == adj
    assert not (copy_ids & original_ids)  # every node is new
    assert Solution().cloneGraph(None) is None
    print("lc133 ok")
