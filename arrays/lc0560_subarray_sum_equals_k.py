"""LeetCode 560. Subarray Sum Equals K (Medium)
Approach: Count prefix sums seen so far; a subarray ending here sums to k when prefix - k was seen before.
Time O(n), space O(n).
"""
from collections import Counter


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        seen, total, count = Counter({0: 1}), 0, 0
        for x in nums:
            total += x
            count += seen[total - k]
            seen[total] += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
    assert s.subarraySum([1, -1, 0], 0) == 3
    print("lc560 ok")
