"""LeetCode 438. Find All Anagrams in a String (Medium)
Approach: fixed-size sliding window of letter counts; record each start where counts match p.
Time O(|s| * alphabet), space O(alphabet).
"""
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        k = len(p)
        if k > len(s):
            return []
        need = Counter(p)
        window = Counter(s[:k])
        res = [0] if window == need else []
        for i in range(k, len(s)):
            window[s[i]] += 1
            old = s[i - k]
            window[old] -= 1
            if window[old] == 0:
                del window[old]
            if window == need:
                res.append(i - k + 1)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert s.findAnagrams("abab", "ab") == [0, 1, 2]
    print("lc438 ok")
