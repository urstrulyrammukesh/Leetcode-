"""LeetCode 90. Subsets II (Medium)
Approach: Sort; when a number repeats, only extend the subsets made in the previous step.
Time O(n * 2^n), space O(n * 2^n).
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        out, start = [[]], 0
        for i, x in enumerate(nums):
            begin = start if i and x == nums[i - 1] else 0
            start = len(out)
            out += [s + [x] for s in out[begin:]]
        return out


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.subsetsWithDup([1, 2, 2])) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    assert s.subsetsWithDup([0]) == [[], [0]]
    print("lc90 ok")
