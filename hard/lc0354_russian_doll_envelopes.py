"""LeetCode 354. Russian Doll Envelopes (Hard)
Approach: sort by width ascending and height descending (so equal widths cannot nest), then LIS on heights.
Time O(n log n), space O(n).
"""
import bisect


class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        tails = []
        for _, h in envelopes:
            idx = bisect.bisect_left(tails, h)
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h
        return len(tails)


if __name__ == "__main__":
    s = Solution()
    assert s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]) == 3
    assert s.maxEnvelopes([[1, 1], [1, 1], [1, 1]]) == 1
    print("lc354 ok")
