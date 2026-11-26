"""LeetCode 410. Split Array Largest Sum (Hard)
Approach: binary search on the answer. For a cap, greedily count how many pieces are needed.
Time O(n log(sum)), space O(1).
"""


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def pieces_needed(cap):
            count, cur = 1, 0
            for x in nums:
                if cur + x > cap:
                    count += 1
                    cur = x
                else:
                    cur += x
            return count

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if pieces_needed(mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert s.splitArray([7, 2, 5, 10, 8], 2) == 18
    assert s.splitArray([1, 2, 3, 4, 5], 2) == 9
    assert s.splitArray([1, 4, 4], 3) == 4
    print("lc410 ok")
