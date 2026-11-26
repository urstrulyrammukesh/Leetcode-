"""LeetCode 51. N-Queens (Hard)
Approach: backtracking row by row, tracking used columns and both diagonals (r - c and r + c).
Time O(n!), space O(n).
"""


class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []
        cols, diag1, diag2 = set(), set(), set()
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or r - c in diag1 or r + c in diag2:
                    continue
                cols.add(c); diag1.add(r - c); diag2.add(r + c)
                board[r][c] = "Q"
                backtrack(r + 1)
                board[r][c] = "."
                cols.remove(c); diag1.remove(r - c); diag2.remove(r + c)

        backtrack(0)
        return res


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.solveNQueens(4)) == sorted([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    assert s.solveNQueens(1) == [["Q"]]
    assert len(s.solveNQueens(8)) == 92
    print("lc51 ok")
