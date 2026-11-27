"""LeetCode 47. Permutations II (Medium)
Approach: Count each value and place values from the counter, so duplicates never produce the same permutation twice.
Time O(n * n!), space O(n).
"""
from collections import Counter


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        count, out, path = Counter(nums), [], []

        def go():
            if len(path) == len(nums):
                out.append(path[:])
                return
            for x in count:
                if count[x]:
                    count[x] -= 1
                    path.append(x)
                    go()
                    path.pop()
                    count[x] += 1

        go()
        return out


if __name__ == "__main__":
    s = Solution()
    assert sorted(s.permuteUnique([1, 1, 2])) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert len(s.permuteUnique([1, 2, 3])) == 6
    print("lc47 ok")
