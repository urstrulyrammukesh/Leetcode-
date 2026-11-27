"""LeetCode 692. Top K Frequent Words (Medium)
Approach: Count words, then take the k smallest by (-count, word) so ties sort alphabetically.
Time O(n log k), space O(n).
"""
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        return heapq.nsmallest(k, count, key=lambda w: (-count[w], w))


if __name__ == "__main__":
    s = Solution()
    assert s.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
    assert s.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
    print("lc692 ok")
