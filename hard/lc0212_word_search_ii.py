"""LeetCode 212. Word Search II (Hard)
Approach: build a trie of the words, then DFS from every cell, walking the trie and the board together.
Time O(rows * cols * 4^L), space O(total word length).
"""


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = {}
        for w in words:
            node = trie
            for ch in w:
                node = node.setdefault(ch, {})
            node["$"] = w
        rows, cols = len(board), len(board[0])
        found = []

        def dfs(r, c, node):
            ch = board[r][c]
            nxt = node.get(ch)
            if not nxt:
                return
            if "$" in nxt:
                found.append(nxt.pop("$"))  # pop so each word is reported once
            board[r][c] = "#"
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, nxt)
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)
        return found


if __name__ == "__main__":
    s = Solution()
    board = [list("oaan"), list("etae"), list("ihkr"), list("iflv")]
    assert sorted(s.findWords(board, ["oath", "pea", "eat", "rain"])) == ["eat", "oath"]
    assert s.findWords([list("ab"), list("cd")], ["abcb"]) == []
    print("lc212 ok")
