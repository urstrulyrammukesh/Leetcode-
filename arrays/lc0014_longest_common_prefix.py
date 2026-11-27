"""LeetCode 14. Longest Common Prefix (Easy)
Approach: Sort the words; the common prefix of the whole list is the common prefix of the first and last word.
Time O(n log n * m), space O(1) extra.
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        a, b = min(strs), max(strs)
        i = 0
        while i < len(a) and a[i] == b[i]:
            i += 1
        return a[:i]


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix(["a"]) == "a"
    print("lc14 ok")
