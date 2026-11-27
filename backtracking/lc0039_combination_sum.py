"""LeetCode 39. Combination Sum (Medium)
Approach: Backtrack over sorted candidates; reuse is allowed, so recurse from the same index.
Time exponential, space O(target / min).
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        out, path = [], []

        def go(start, rest):
            if rest == 0:
                out.append(path[:])
                return
            for i in range(start, len(candidates)):
                c = candidates[i]
                if c > rest:
                    break
                path.append(c)
                go(i, rest - c)
                path.pop()

        go(0, target)
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert s.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert s.combinationSum([2], 1) == []
    print("lc39 ok")
