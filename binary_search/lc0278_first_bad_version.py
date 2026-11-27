"""LeetCode 278. First Bad Version (Easy)
Approach: Binary search for the first version where isBadVersion is true.
Time O(log n), space O(1).
"""


class Solution:
    def __init__(self, bad=1):
        self.bad = bad

    def isBadVersion(self, v: int) -> bool:  # given by LeetCode
        return v >= self.bad

    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if self.isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == "__main__":
    s = Solution()
    assert Solution(bad=4).firstBadVersion(5) == 4
    assert Solution(bad=1).firstBadVersion(1) == 1
    assert Solution(bad=1702766719).firstBadVersion(2126753390) == 1702766719
    print("lc278 ok")
