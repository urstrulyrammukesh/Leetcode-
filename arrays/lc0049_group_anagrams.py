"""LeetCode 49. Group Anagrams (Medium)
Approach: Words that are anagrams share the same sorted letters; group by that key.
Time O(n * k log k), space O(n * k).
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for w in strs:
            groups["".join(sorted(w))].append(w)
        return list(groups.values())


if __name__ == "__main__":
    s = Solution()
    out = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(sorted(g) for g in out) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert s.groupAnagrams([""]) == [[""]]
    print("lc49 ok")
