"""LeetCode 767. Reorganize String (Medium)
Approach: Always place the most frequent remaining letter that differs from the last one placed (max-heap).
Time O(n log a), space O(a).
"""
import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [(-c, ch) for ch, c in Counter(s).items()]
        heapq.heapify(heap)
        out, held = [], None
        while heap:
            c, ch = heapq.heappop(heap)
            out.append(ch)
            if held:
                heapq.heappush(heap, held)
                held = None
            if c + 1 < 0:
                held = (c + 1, ch)
        return "".join(out) if not held else ""


if __name__ == "__main__":
    s = Solution()
    r = s.reorganizeString("aab")
    assert sorted(r) == ["a", "a", "b"] and all(a != b for a, b in zip(r, r[1:]))
    assert s.reorganizeString("aaab") == ""
    print("lc767 ok")
