"""LeetCode 205. Isomorphic Strings (Easy)
Approach: Map characters both ways; a clash in either map means the strings are not isomorphic.
Time O(n), space O(1) (alphabet size).
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a, b = {}, {}
        for x, y in zip(s, t):
            if a.setdefault(x, y) != y or b.setdefault(y, x) != x:
                return False
        return len(s) == len(t)


if __name__ == "__main__":
    s = Solution()
    assert s.isIsomorphic("egg", "add")
    assert not s.isIsomorphic("foo", "bar")
    assert s.isIsomorphic("paper", "title")
    assert not s.isIsomorphic("badc", "baba")
    print("lc205 ok")
