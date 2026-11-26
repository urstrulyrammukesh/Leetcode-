"""LeetCode 76. Minimum Window Substring (Hard)
Approach: sliding window with a count of characters still missing; shrink from the left once the window is valid.
Time O(|s| + |t|), space O(alphabet).
"""
from collections import Counter
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = 0
        best = (0, inf)
        for right, ch in enumerate(s, 1):
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            if missing == 0:
                while need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                if right - left < best[1] - best[0]:
                    best = (left, right)
                need[s[left]] += 1
                missing += 1
                left += 1
        return "" if best[1] == inf else s[best[0]:best[1]]


if __name__ == "__main__":
    s = Solution()
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("a", "a") == "a"
    assert s.minWindow("a", "aa") == ""
    print("lc76 ok")
