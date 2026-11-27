"""LeetCode 66. Plus One (Easy)
Approach: Add one from the right; 9 becomes 0 and carries, otherwise stop.
Time O(n), space O(1) (O(n) when a new digit is needed).
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits


if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([9, 9]) == [1, 0, 0]
    print("lc66 ok")
