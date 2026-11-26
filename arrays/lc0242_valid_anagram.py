"""LeetCode 242. Valid Anagram (Easy)
Approach: two strings are anagrams when every character appears the same number of times.
Time O(n), space O(alphabet).
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram")
    assert not s.isAnagram("rat", "car")
    print("lc242 ok")
