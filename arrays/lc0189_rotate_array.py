"""LeetCode 189. Rotate Array (Medium)
Approach: reverse the whole array, then reverse the first k and the rest.
Time O(n), space O(1).
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]
    b = [-1, -100, 3, 99]
    Solution().rotate(b, 2)
    assert b == [3, 99, -1, -100]
    c = [1, 2]
    Solution().rotate(c, 5)
    assert c == [2, 1]
    print("lc189 ok")
