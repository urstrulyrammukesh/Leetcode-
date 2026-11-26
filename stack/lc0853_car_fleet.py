"""LeetCode 853. Car Fleet (Medium)
Approach: go from the car nearest the target backwards; a car that would arrive no later than the fleet ahead joins it.
Time O(n log n), space O(n).
"""


class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        fleets = []
        for p, s in sorted(zip(position, speed), reverse=True):
            time = (target - p) / s
            if not fleets or time > fleets[-1]:
                fleets.append(time)
        return len(fleets)


if __name__ == "__main__":
    s = Solution()
    assert s.carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert s.carFleet(10, [3], [3]) == 1
    assert s.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
    print("lc853 ok")
