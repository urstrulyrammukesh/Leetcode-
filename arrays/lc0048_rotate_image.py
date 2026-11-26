"""LeetCode 48. Rotate Image (Medium)
Approach: transpose the matrix, then reverse each row. That is a 90 degree clockwise rotation, in place.
Time O(n^2), space O(1).
"""


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    print("lc48 ok")
