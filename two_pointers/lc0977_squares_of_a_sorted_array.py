"""LeetCode 977. Squares of a Sorted Array (Easy)
Approach: The biggest square is at one of the two ends; fill the answer from the back.
Time O(n), space O(n) for the output.
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        out = [0] * len(nums)
        i, j = 0, len(nums) - 1
        for k in range(len(nums) - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                out[k] = nums[i] ** 2
                i += 1
            else:
                out[k] = nums[j] ** 2
                j -= 1
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
    assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
    print("lc977 ok")
