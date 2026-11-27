"""LeetCode 1004. Max Consecutive Ones III (Medium)
Approach: Longest window with at most k zeros: move the left edge whenever there are too many zeros.
Time O(n), space O(1).
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left = zeros = best = 0
        for right, x in enumerate(nums):
            zeros += x == 0
            while zeros > k:
                zeros -= nums[left] == 0
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
    assert s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
    print("lc1004 ok")
