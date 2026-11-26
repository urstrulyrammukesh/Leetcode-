"""LeetCode 347. Top K Frequent Elements (Medium)
Approach: bucket sort by frequency; bucket i holds the numbers that appear i times.
Time O(n), space O(n).
"""
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        for x, c in Counter(nums).items():
            buckets[c].append(x)
        out = []
        for c in range(len(buckets) - 1, 0, -1):
            for x in buckets[c]:
                out.append(x)
                if len(out) == k:
                    return out
        return out


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert s.topKFrequent([1], 1) == [1]
    print("lc347 ok")
