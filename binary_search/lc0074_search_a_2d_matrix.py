"""LeetCode 74. Search a 2D Matrix (Medium)
Approach: the rows join into one sorted list, so binary search index i as cell (i // cols, i % cols).
Time O(log(m * n)), space O(1).
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows * cols - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            v = matrix[mid // cols][mid % cols]
            if v == target:
                return True
            if v < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False


if __name__ == "__main__":
    s = Solution()
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert s.searchMatrix(m, 3)
    assert not s.searchMatrix(m, 13)
    print("lc74 ok")
