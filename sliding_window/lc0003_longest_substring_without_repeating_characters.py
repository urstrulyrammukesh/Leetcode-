"""LeetCode 3. Longest Substring Without Repeating Characters (Medium)
Approach: Keep the last index of each character; when a repeat appears inside the window, move the left edge past it.
Time O(n), space O(alphabet).
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last, left, best = {}, 0, 0
        for i, c in enumerate(s):
            if last.get(c, -1) >= left:
                left = last[c] + 1
            last[c] = i
            best = max(best, i - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring("") == 0
    print("lc3 ok")
