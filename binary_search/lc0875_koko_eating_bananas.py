"""LeetCode 875. Koko Eating Bananas (Medium)
Approach: binary search on the eating speed k; a speed works if the total hours sum(ceil(p / k)) fit in h.
Time O(n log(max pile)), space O(1).
"""


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (lo + hi) // 2
            hours = sum((p + k - 1) // k for p in piles)
            if hours <= h:
                hi = k
            else:
                lo = k + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    print("lc875 ok")
