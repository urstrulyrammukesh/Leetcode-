"""LeetCode 127. Word Ladder (Hard)
Approach: BFS from beginWord; neighbours are dictionary words that differ by one letter.
Time O(N * L * 26), space O(N).
"""
from collections import deque
from string import ascii_lowercase


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in ascii_lowercase:
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in words and nxt not in seen:
                        seen.add(nxt)
                        queue.append((nxt, steps + 1))
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == 5
    assert s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("lc127 ok")
