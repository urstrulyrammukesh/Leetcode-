"""LeetCode 73. Set Matrix Zeroes (Medium)
Approach: first record which rows and columns hold a zero, then clear them in a second pass.
Time O(m * n), space O(m + n).
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        zero_rows, zero_cols = set(), set()
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                if v == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        for r, row in enumerate(matrix):
            for c in range(len(row)):
                if r in zero_rows or c in zero_cols:
                    row[c] = 0


if __name__ == "__main__":
    a = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(a)
    assert a == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    b = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(b)
    assert b == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    print("lc73 ok")
