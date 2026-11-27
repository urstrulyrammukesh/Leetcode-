"""LeetCode 846. Hand of Straights (Medium)
Approach: Always start a group at the smallest card left and take the next groupSize consecutive cards.
Time O(n log n), space O(n).
"""
from collections import Counter


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        count = Counter(hand)
        for x in sorted(count):
            k = count[x]
            if k:
                for y in range(x, x + groupSize):
                    if count[y] < k:
                        return False
                    count[y] -= k
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
    assert not s.isNStraightHand([1, 2, 3, 4, 5], 4)
    print("lc846 ok")
