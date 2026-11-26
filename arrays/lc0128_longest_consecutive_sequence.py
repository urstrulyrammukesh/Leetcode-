"""LeetCode 128. Longest Consecutive Sequence (Medium)
Approach: put numbers in a set and only start counting at x when x - 1 is missing (the start of a run).
Time O(n), space O(n).
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        best = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                length = 1
                while x + length in nums_set:
                    length += 1
                best = max(best, length)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert s.longestConsecutive([]) == 0
    print("lc128 ok")
