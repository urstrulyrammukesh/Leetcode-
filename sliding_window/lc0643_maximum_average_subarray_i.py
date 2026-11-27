"""LeetCode 643. Maximum Average Subarray I (Easy)
Approach: Fixed window of size k: add the new number, drop the one leaving.
Time O(n), space O(1).
"""


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur = best = sum(nums[:k])
        for i in range(k, len(nums)):
            cur += nums[i] - nums[i - k]
            best = max(best, cur)
        return best / k


if __name__ == "__main__":
    s = Solution()
    assert s.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
    assert s.findMaxAverage([5], 1) == 5.0
    print("lc643 ok")
