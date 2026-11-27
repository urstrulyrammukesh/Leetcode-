"""LeetCode 1011. Capacity To Ship Packages Within D Days (Medium)
Approach: Binary search on the answer: the smallest capacity whose greedy loading needs at most `days` days.
Time O(n log(sum)), space O(1).
"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def need(cap):
            d, load = 1, 0
            for w in weights:
                if load + w > cap:
                    d, load = d + 1, 0
                load += w
            return d

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if need(mid) <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15
    assert s.shipWithinDays([3, 2, 2, 4, 1, 4], 3) == 6
    assert s.shipWithinDays([1, 2, 3, 1, 1], 4) == 3
    print("lc1011 ok")
