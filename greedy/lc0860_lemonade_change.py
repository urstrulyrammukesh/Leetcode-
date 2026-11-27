"""LeetCode 860. Lemonade Change (Easy)
Approach: Keep counts of 5s and 10s; give change with a 10 first when possible.
Time O(n), space O(1).
"""


class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = ten = 0
        for b in bills:
            if b == 5:
                five += 1
            elif b == 10:
                five, ten = five - 1, ten + 1
            elif ten:
                five, ten = five - 1, ten - 1
            else:
                five -= 3
            if five < 0:
                return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.lemonadeChange([5, 5, 5, 10, 20])
    assert not s.lemonadeChange([5, 5, 10, 10, 20])
    print("lc860 ok")
