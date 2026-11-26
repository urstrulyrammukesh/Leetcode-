"""LeetCode 217. Contains Duplicate (Easy)
Approach: a set drops repeats, so a duplicate exists when the set is smaller than the list.
Time O(n), space O(n).
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1])
    assert not s.containsDuplicate([1, 2, 3, 4])
    assert s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print("lc217 ok")
