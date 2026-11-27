"""LeetCode 77. Combinations (Medium)
Approach: Pick numbers in increasing order; stop early when not enough numbers are left.
Time O(C(n, k) * k), space O(k).
"""


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        out, path = [], []

        def go(start):
            if len(path) == k:
                out.append(path[:])
                return
            for x in range(start, n - (k - len(path)) + 2):
                path.append(x)
                go(x + 1)
                path.pop()

        go(1)
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    assert s.combine(1, 1) == [[1]]
    print("lc77 ok")
