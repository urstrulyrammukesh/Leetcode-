"""LeetCode 216. Combination Sum III (Medium)
Approach: Choose k distinct digits 1-9 in increasing order that add up to n.
Time O(C(9, k)), space O(k).
"""
from itertools import combinations


class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        return [list(c) for c in combinations(range(1, 10), k) if sum(c) == n]


if __name__ == "__main__":
    s = Solution()
    assert s.combinationSum3(3, 7) == [[1, 2, 4]]
    assert s.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert s.combinationSum3(4, 1) == []
    print("lc216 ok")
