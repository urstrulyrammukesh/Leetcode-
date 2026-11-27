"""LeetCode 735. Asteroid Collision (Medium)
Approach: Stack of survivors; a left-moving asteroid destroys smaller right-movers on top of the stack.
Time O(n), space O(n).
"""


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                if stack[-1] == -a:
                    stack.pop()
                alive = False
            if alive:
                stack.append(a)
        return stack


if __name__ == "__main__":
    s = Solution()
    assert s.asteroidCollision([5, 10, -5]) == [5, 10]
    assert s.asteroidCollision([8, -8]) == []
    assert s.asteroidCollision([10, 2, -5]) == [10]
    assert s.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]
    print("lc735 ok")
