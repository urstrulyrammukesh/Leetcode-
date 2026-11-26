"""LeetCode 85. Maximal Rectangle (Hard)
Approach: treat each row as the base of a histogram of consecutive '1's above it, then reuse Largest Rectangle in Histogram.
Time O(rows * cols), space O(cols).
"""


class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        heights = [0] * len(matrix[0])
        best = 0
        for row in matrix:
            for c, v in enumerate(row):
                heights[c] = heights[c] + 1 if v == "1" else 0
            best = max(best, self._largest(heights))
        return best

    @staticmethod
    def _largest(heights):
        stack, best = [], 0
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                best = max(best, height * (i - idx))
                start = idx
            stack.append((start, h))
        return best


if __name__ == "__main__":
    s = Solution()
    grid = [list("10100"), list("10111"), list("11111"), list("10010")]
    assert s.maximalRectangle(grid) == 6
    assert s.maximalRectangle([["0"]]) == 0
    assert s.maximalRectangle([["1"]]) == 1
    print("lc85 ok")
