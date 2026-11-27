"""LeetCode 80. Remove Duplicates from Sorted Array II (Medium)
Approach: Write pointer: keep x unless it equals the value two slots back (that would make three).
Time O(n), space O(1).
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for x in nums:
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    a = [1, 1, 1, 2, 2, 3]
    k = s.removeDuplicates(a)
    assert k == 5 and a[:k] == [1, 1, 2, 2, 3]
    b = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = s.removeDuplicates(b)
    assert k == 7 and b[:k] == [0, 0, 1, 1, 2, 3, 3]
    print("lc80 ok")
