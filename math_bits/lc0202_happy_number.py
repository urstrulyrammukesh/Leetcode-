"""LeetCode 202. Happy Number (Easy)
Approach: Repeat 'sum of squared digits'; Floyd's cycle check stops at 1 or at a loop.
Time O(log n) per step, space O(1).
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        step = lambda x: sum(int(d) ** 2 for d in str(x))
        slow, fast = n, step(n)
        while fast != 1 and slow != fast:
            slow, fast = step(slow), step(step(fast))
        return fast == 1


if __name__ == "__main__":
    s = Solution()
    assert s.isHappy(19)
    assert not s.isHappy(2)
    print("lc202 ok")
