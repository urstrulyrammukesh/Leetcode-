"""LeetCode 88. Merge Sorted Array (Easy)
Approach: Fill nums1 from the back with the larger of the two tails, so nothing is overwritten.
Time O(m + n), space O(1).
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i, j, k = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3, 0, 0, 0]
    s.merge(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]
    b = [0]
    s.merge(b, 0, [1], 1)
    assert b == [1]
    print("lc88 ok")
