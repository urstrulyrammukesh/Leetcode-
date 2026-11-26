"""LeetCode 37. Sudoku Solver (Hard)
Approach: backtracking over empty cells, with sets for rows, columns and boxes so each check is O(1).
Time exponential in the worst case, fast in practice; space O(81).
"""


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    empty.append((r, c))
                else:
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[(r // 3) * 3 + c // 3].add(v)

        def backtrack(i):
            if i == len(empty):
                return True
            r, c = empty[i]
            b = (r // 3) * 3 + c // 3
            for d in "123456789":
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    continue
                board[r][c] = d
                rows[r].add(d); cols[c].add(d); boxes[b].add(d)
                if backtrack(i + 1):
                    return True
                rows[r].remove(d); cols[c].remove(d); boxes[b].remove(d)
                board[r][c] = "."
            return False

        backtrack(0)


if __name__ == "__main__":
    puzzle = [
        "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1",
        "7...2...6", ".6....28.", "...419..5", "....8..79",
    ]
    board = [list(row) for row in puzzle]
    Solution().solveSudoku(board)
    digits = set("123456789")
    assert all(set(row) == digits for row in board)
    assert all({board[r][c] for r in range(9)} == digits for c in range(9))
    assert all({board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)} == digits
               for br in (0, 3, 6) for bc in (0, 3, 6))
    assert all(puzzle[r][c] in (".", board[r][c]) for r in range(9) for c in range(9))
    print("lc37 ok")
