"""LeetCode 27. Remove Element (Easy)
Approach: Write pointer: copy every value that is not val to the front.
Time O(n), space O(1).
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k


if __name__ == "__main__":
    s = Solution()
    a = [0, 1, 2, 2, 3, 0, 4, 2]
    k = s.removeElement(a, 2)
    assert k == 5 and sorted(a[:k]) == [0, 0, 1, 3, 4]
    assert s.removeElement([], 1) == 0
    print("lc27 ok")
