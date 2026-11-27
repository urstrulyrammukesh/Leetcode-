"""LeetCode 139. Word Break (Medium)
Approach: ok[i] is true when some word ends at i and ok[i - len(word)] is true.
Time O(n * words * L), space O(n).
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        ok = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            ok[i] = any(ok[i - len(w)] and s[i - len(w):i] == w for w in wordDict if len(w) <= i)
        return ok[-1]


if __name__ == "__main__":
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"])
    assert s.wordBreak("applepenapple", ["apple", "pen"])
    assert not s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    print("lc139 ok")
