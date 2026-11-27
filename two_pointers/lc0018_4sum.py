"""LeetCode 18. 4Sum (Medium)
Approach: Sort, fix two numbers with two loops, then two pointers on the rest, skipping duplicates.
Time O(n^3), space O(1) extra.
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n, out = len(nums), []
        for i in range(n):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                lo, hi = j + 1, n - 1
                while lo < hi:
                    t = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if t < target:
                        lo += 1
                    elif t > target:
                        hi -= 1
                    else:
                        out.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.fourSum([1, 0, -1, 0, -2, 2], 0) == [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert s.fourSum([2, 2, 2, 2, 2], 8) == [[2, 2, 2, 2]]
    print("lc18 ok")
