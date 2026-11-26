"""LeetCode 448. Find All Numbers Disappeared in an Array (Easy)
Approach: for every value v, mark index v-1 by making it negative; positive indexes are the missing numbers.
Time O(n), space O(1) extra.
"""


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for x in nums:
            i = abs(x) - 1
            nums[i] = -abs(nums[i])
        return [i + 1 for i, x in enumerate(nums) if x > 0]


if __name__ == "__main__":
    s = Solution()
    assert s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert s.findDisappearedNumbers([1, 1]) == [2]
    print("lc448 ok")
