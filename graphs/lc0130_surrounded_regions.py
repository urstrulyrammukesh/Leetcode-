"""LeetCode 130. Surrounded Regions (Medium)
Approach: Mark every 'O' connected to the border as safe; flip the rest to 'X'.
Time O(m * n), space O(m * n).
"""


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        R, C = len(board), len(board[0])
        stack = [(r, c) for r in range(R) for c in range(C) if (r in (0, R - 1) or c in (0, C - 1)) and board[r][c] == "O"]
        while stack:
            r, c = stack.pop()
            if 0 <= r < R and 0 <= c < C and board[r][c] == "O":
                board[r][c] = "S"
                stack += [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        for r in range(R):
            for c in range(C):
                board[r][c] = "O" if board[r][c] == "S" else "X"


if __name__ == "__main__":
    s = Solution()
    b = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    s.solve(b)
    assert b == [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]
    print("lc130 ok")
