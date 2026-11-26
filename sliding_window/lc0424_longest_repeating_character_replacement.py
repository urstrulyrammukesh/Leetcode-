"""LeetCode 424. Longest Repeating Character Replacement (Medium)
Approach: sliding window. A window is fine while (length - count of its most common letter) <= k.
Time O(n), space O(alphabet).
"""
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = max_freq = best = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            max_freq = max(max_freq, count[ch])
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.characterReplacement("ABAB", 2) == 4
    assert s.characterReplacement("AABABBA", 1) == 4
    print("lc424 ok")
