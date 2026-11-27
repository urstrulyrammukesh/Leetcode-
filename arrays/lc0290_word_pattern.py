"""LeetCode 290. Word Pattern (Easy)
Approach: Same idea as isomorphic strings, with letters on one side and words on the other.
Time O(n), space O(n).
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        a, b = {}, {}
        for c, w in zip(pattern, words):
            if a.setdefault(c, w) != w or b.setdefault(w, c) != c:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.wordPattern("abba", "dog cat cat dog")
    assert not s.wordPattern("abba", "dog cat cat fish")
    assert not s.wordPattern("aaaa", "dog cat cat dog")
    assert not s.wordPattern("abba", "dog dog dog dog")
    print("lc290 ok")
