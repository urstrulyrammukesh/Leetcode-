"""LeetCode 140. Word Break II (Hard)
Approach: DFS with memoisation; go(i) returns every sentence that spells s[i:].
Time exponential in the number of answers, space O(n * answers).
"""
from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)

        @lru_cache(maxsize=None)
        def go(i):
            if i == len(s):
                return [""]
            out = []
            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in words:
                    for rest in go(j):
                        out.append(word + (" " + rest if rest else ""))
            return out

        return go(0)


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])) == ["cat sand dog", "cats and dog"]
    assert sorted(s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])) == [
        "pine apple pen apple", "pine applepen apple", "pineapple pen apple"]
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == []
    print("lc140 ok")
