"""LeetCode 567. Permutation in String (Medium)
Approach: slide a window of len(s1) over s2 and compare letter counts.
Time O(|s2| * alphabet), space O(alphabet).
"""
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        need = Counter(s1)
        window = Counter(s2[:k])
        if window == need:
            return True
        for i in range(k, len(s2)):
            window[s2[i]] += 1
            old = s2[i - k]
            window[old] -= 1
            if window[old] == 0:
                del window[old]
            if window == need:
                return True
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.checkInclusion("ab", "eidbaooo")
    assert not s.checkInclusion("ab", "eidboaoo")
    assert not s.checkInclusion("abc", "ab")
    print("lc567 ok")
