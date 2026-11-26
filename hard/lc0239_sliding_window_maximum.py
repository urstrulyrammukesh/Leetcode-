"""LeetCode 239. Sliding Window Maximum (Hard)
Approach: monotonic deque of indices with decreasing values; the front is always the window's maximum.
Time O(n), space O(k).
"""
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        out = []
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] <= x:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert s.maxSlidingWindow([1], 1) == [1]
    assert s.maxSlidingWindow([9, 8, 7, 6], 2) == [9, 8, 7]
    print("lc239 ok")
