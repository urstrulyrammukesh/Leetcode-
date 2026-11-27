"""LeetCode 57. Insert Interval (Medium)
Approach: Copy intervals that end before the new one, merge every overlapping one into it, then copy the rest.
Time O(n), space O(n).
"""


class Solution:
    def insert(self, intervals: list[list[int]], new: list[int]) -> list[list[int]]:
        out, i, n = [], 0, len(intervals)
        a, b = new
        while i < n and intervals[i][1] < a:
            out.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= b:
            a, b = min(a, intervals[i][0]), max(b, intervals[i][1])
            i += 1
        out.append([a, b])
        return out + intervals[i:]


if __name__ == "__main__":
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert s.insert([], [5, 7]) == [[5, 7]]
    print("lc57 ok")
