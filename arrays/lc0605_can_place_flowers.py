"""LeetCode 605. Can Place Flowers (Easy)
Approach: Walk the bed and plant greedily wherever the spot and both neighbours are empty.
Time O(n), space O(1).
"""


class Solution:
    def canPlaceFlowers(self, bed: list[int], n: int) -> bool:
        bed = [0] + bed + [0]
        for i in range(1, len(bed) - 1):
            if bed[i - 1] == bed[i] == bed[i + 1] == 0:
                bed[i] = 1
                n -= 1
        return n <= 0


if __name__ == "__main__":
    s = Solution()
    assert s.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    assert not s.canPlaceFlowers([1, 0, 0, 0, 1], 2)
    assert s.canPlaceFlowers([0], 1)
    print("lc605 ok")
