"""LeetCode 135. Candy (Hard)
Approach: two passes. Left-to-right fixes the rule against the left neighbour, right-to-left against the right one.
Time O(n), space O(n).
"""


class Solution:
    def candy(self, ratings: list[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        return sum(candies)


if __name__ == "__main__":
    s = Solution()
    assert s.candy([1, 0, 2]) == 5
    assert s.candy([1, 2, 2]) == 4
    assert s.candy([1, 3, 2, 2, 1]) == 7
    print("lc135 ok")
