"""LeetCode 46. Permutations (Medium)
Approach: Swap each remaining number into the current position and recurse.
Time O(n * n!), space O(n).
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        out = []

        def go(i):
            if i == len(nums):
                out.append(nums[:])
                return
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                go(i + 1)
                nums[i], nums[j] = nums[j], nums[i]

        go(0)
        return out


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.permute([1, 2, 3])) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert s.permute([1]) == [[1]]
    print("lc46 ok")
