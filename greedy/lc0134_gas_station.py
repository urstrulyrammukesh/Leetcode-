"""LeetCode 134. Gas Station (Medium)
Approach: If total gas >= total cost a start exists; restart after any point where the tank goes negative.
Time O(n), space O(1).
"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = tank = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            tank += g - c
            if tank < 0:
                start, tank = i + 1, 0
        return start


if __name__ == "__main__":
    s = Solution()
    assert s.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert s.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    print("lc134 ok")
