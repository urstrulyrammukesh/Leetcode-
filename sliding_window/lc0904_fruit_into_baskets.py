"""LeetCode 904. Fruit Into Baskets (Medium)
Approach: Longest window with at most two distinct values: shrink from the left when a third type appears.
Time O(n), space O(1).
"""
from collections import Counter


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        count, left, best = Counter(), 0, 0
        for right, f in enumerate(fruits):
            count[f] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if not count[fruits[left]]:
                    del count[fruits[left]]
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == "__main__":
    s = Solution()
    assert s.totalFruit([1, 2, 1]) == 3
    assert s.totalFruit([0, 1, 2, 2]) == 3
    assert s.totalFruit([1, 2, 3, 2, 2]) == 4
    print("lc904 ok")
