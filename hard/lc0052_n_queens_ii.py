"""LeetCode 52. N-Queens II (Hard)
Approach: same backtracking as N-Queens, but only count the boards.
Time O(n!), space O(n).
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, diag1, diag2 = set(), set(), set()

        def backtrack(r):
            if r == n:
                return 1
            count = 0
            for c in range(n):
                if c in cols or r - c in diag1 or r + c in diag2:
                    continue
                cols.add(c); diag1.add(r - c); diag2.add(r + c)
                count += backtrack(r + 1)
                cols.remove(c); diag1.remove(r - c); diag2.remove(r + c)
            return count

        return backtrack(0)


if __name__ == "__main__":
    s = Solution()
    assert [s.totalNQueens(n) for n in (1, 4, 8)] == [1, 2, 92]
    print("lc52 ok")
