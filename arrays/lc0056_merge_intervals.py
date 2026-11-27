"""LeetCode 56. Merge Intervals (Medium)
Approach: Sort by start; extend the last merged interval while the next one overlaps it.
Time O(n log n), space O(n).
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        out = []
        for a, b in sorted(intervals):
            if out and a <= out[-1][1]:
                out[-1][1] = max(out[-1][1], b)
            else:
                out.append([a, b])
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert s.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert s.merge([[1, 4], [0, 4]]) == [[0, 4]]
    print("lc56 ok")
