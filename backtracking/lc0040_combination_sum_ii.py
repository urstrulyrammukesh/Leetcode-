"""LeetCode 40. Combination Sum II (Medium)
Approach: Sort; each number used once, and skip equal numbers at the same depth to avoid duplicate sets.
Time exponential, space O(n).
"""


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        out, path = [], []

        def go(start, rest):
            if rest == 0:
                out.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > rest:
                    break
                path.append(candidates[i])
                go(i + 1, rest - candidates[i])
                path.pop()

        go(0, target)
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert s.combinationSum2([2, 5, 2, 1, 2], 5) == [[1, 2, 2], [5]]
    print("lc40 ok")
