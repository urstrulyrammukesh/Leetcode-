"""LeetCode 169. Majority Element (Easy)
Approach: Boyer-Moore voting. The majority survives every pairwise cancellation.
Time O(n), space O(1).
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate, count = None, 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    print("lc169 ok")
