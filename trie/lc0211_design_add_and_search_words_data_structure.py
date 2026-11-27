"""LeetCode 211. Design Add and Search Words Data Structure (Medium)
Approach: A trie; '.' branches into every child during search.
Time O(L) to add, up to O(26^L) to search, space O(total letters).
"""


class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        def go(node, i):
            if i == len(word):
                return "$" in node
            c = word[i]
            if c == ".":
                return any(go(child, i + 1) for k, child in node.items() if k != "$")
            return c in node and go(node[c], i + 1)

        return go(self.root, 0)


if __name__ == "__main__":
    w = WordDictionary()
    for x in ("bad", "dad", "mad"):
        w.addWord(x)
    assert not w.search("pad") and w.search("bad") and w.search(".ad") and w.search("b..")
    print("lc211 ok")
