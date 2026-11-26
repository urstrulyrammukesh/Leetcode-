"""LeetCode 149. Max Points on a Line (Hard)
Approach: for each point, count the others by reduced slope (dx, dy) using gcd so no floating point is needed.
Time O(n^2 log C), space O(n).
"""
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        best = 0
        for i in range(n):
            slopes = defaultdict(int)
            x1, y1 = points[i]
            for j in range(i + 1, n):
                dx, dy = points[j][0] - x1, points[j][1] - y1
                g = gcd(dx, dy)
                dx, dy = dx // g, dy // g
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy
                slopes[(dx, dy)] += 1
            if slopes:
                best = max(best, max(slopes.values()) + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.maxPoints([[1, 1], [2, 2], [3, 3]]) == 3
    assert s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]) == 4
    assert s.maxPoints([[0, 0]]) == 1
    print("lc149 ok")
