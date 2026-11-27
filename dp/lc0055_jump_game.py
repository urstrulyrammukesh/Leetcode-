"""LeetCode 55. Jump Game (Medium)
Approach: Track the furthest index reachable so far; fail if we ever stand beyond it.
Time O(n), space O(1).
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        far = 0
        for i, x in enumerate(nums):
            if i > far:
                return False
            far = max(far, i + x)
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.canJump([2, 3, 1, 1, 4])
    assert not s.canJump([3, 2, 1, 0, 4])
    print("lc55 ok")
