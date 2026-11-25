"""LeetCode 209. Minimum Size Subarray Sum. Sliding window over positive numbers. O(n) time, O(1) space."""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        best = float("inf")
        left = total = 0
        for right, x in enumerate(nums):
            total += x
            while total >= target:
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best == float("inf") else best

if __name__ == "__main__":
    s = Solution()
    assert s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert s.minSubArrayLen(4, [1, 4, 4]) == 1
    assert s.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    print("lc209 ok")
