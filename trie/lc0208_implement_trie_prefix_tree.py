"""LeetCode 208. Implement Trie (Prefix Tree) (Medium)
Approach: Nested dicts, one level per letter; a special key marks the end of a word.
Time O(L) per operation, space O(total letters).
"""


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def _walk(self, s):
        node = self.root
        for c in s:
            if c not in node:
                return None
            node = node[c]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return bool(node and node.get("$"))

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    assert t.search("apple") and not t.search("app") and t.startsWith("app")
    t.insert("app")
    assert t.search("app")
    print("lc208 ok")
