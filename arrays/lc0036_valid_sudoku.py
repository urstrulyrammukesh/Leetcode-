"""LeetCode 36. Valid Sudoku (Medium)
Approach: one pass with sets for each row, column and 3x3 box; any repeat makes the board invalid.
Time O(81), space O(81).
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue
                b = (r // 3) * 3 + c // 3
                if v in rows[r] or v in cols[c] or v in boxes[b]:
                    return False
                rows[r].add(v)
                cols[c].add(v)
                boxes[b].add(v)
        return True


if __name__ == "__main__":
    puzzle = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
              "7...2...6", ".6....28.", "...419..5", "....8..79"]
    board = [list(row) for row in puzzle]
    assert Solution().isValidSudoku(board)
    board[0][0] = "8"  # clashes with the 8 lower in column 0
    assert not Solution().isValidSudoku(board)
    print("lc36 ok")
