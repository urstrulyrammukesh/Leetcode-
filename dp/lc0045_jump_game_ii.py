"""LeetCode 45. Jump Game II (Medium)
Approach: BFS by layers: each jump covers a range; count how many ranges until the end is reached.
Time O(n), space O(1).
"""


class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = end = far = 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                jumps, end = jumps + 1, far
        return jumps


if __name__ == "__main__":
    s = Solution()
    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([2, 3, 0, 1, 4]) == 2
    assert s.jump([0]) == 0
    print("lc45 ok")
