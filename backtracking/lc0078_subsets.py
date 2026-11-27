"""LeetCode 78. Subsets (Medium)
Approach: Start with the empty set; each number doubles the list by adding itself to every subset so far.
Time O(n * 2^n), space O(n * 2^n).
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        out = [[]]
        for x in nums:
            out += [s + [x] for s in out]
        return out


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.subsets([1, 2, 3])) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    assert s.subsets([0]) == [[], [0]]
    print("lc78 ok")
