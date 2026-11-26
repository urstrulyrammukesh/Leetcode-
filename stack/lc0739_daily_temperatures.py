"""LeetCode 739. Daily Temperatures (Medium)
Approach: monotonic decreasing stack of indices; a warmer day resolves every colder day on the stack.
Time O(n), space O(n).
"""


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res


if __name__ == "__main__":
    s = Solution()
    assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    print("lc739 ok")
