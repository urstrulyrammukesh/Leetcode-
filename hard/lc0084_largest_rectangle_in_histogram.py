"""LeetCode 84. Largest Rectangle in Histogram (Hard)
Approach: monotonic increasing stack of (start index, height); popping a bar closes the rectangle it can extend.
Time O(n), space O(n).
"""


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        best = 0
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
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([2, 4]) == 4
    assert s.largestRectangleArea([1, 1, 1, 1]) == 4
    print("lc84 ok")
