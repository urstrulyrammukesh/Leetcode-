"""LeetCode 79. Word Search (Medium)
Approach: DFS from every cell, marking cells as used on the current path and restoring them on the way back.
Time O(m * n * 3^L), space O(L).
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            found = any(dfs(r + dr, c + dc, i + 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            board[r][c] = word[i]
            return found

        return any(dfs(r, c, 0) for r in range(R) for c in range(C))


if __name__ == "__main__":
    s = Solution()
    b = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert s.exist(b, "ABCCED") and s.exist(b, "SEE") and not s.exist(b, "ABCB")
    print("lc79 ok")
