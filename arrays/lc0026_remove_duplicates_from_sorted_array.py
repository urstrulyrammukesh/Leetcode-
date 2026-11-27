"""LeetCode 26. Remove Duplicates from Sorted Array (Easy)
Approach: A write pointer keeps the next free slot; copy each value that differs from the last kept one.
Time O(n), space O(1).
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for x in nums:
            if k == 0 or x != nums[k - 1]:
                nums[k] = x
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(a)
    assert k == 5 and a[:k] == [0, 1, 2, 3, 4]
    b = [1, 1, 2]
    assert s.removeDuplicates(b) == 2 and b[:2] == [1, 2]
    print("lc26 ok")
