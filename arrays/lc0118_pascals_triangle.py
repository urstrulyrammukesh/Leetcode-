"""LeetCode 118. Pascal's Triangle (Easy)
Approach: Each row starts and ends with 1; every inner value is the sum of the two values above it.
Time O(n^2), space O(n^2) for the output.
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        rows = [[1]]
        for _ in range(numRows - 1):
            prev = rows[-1]
            rows.append([1] + [prev[i] + prev[i + 1] for i in range(len(prev) - 1)] + [1])
        return rows[:numRows]


if __name__ == "__main__":
    s = Solution()
    assert s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert s.generate(1) == [[1]]
    print("lc118 ok")
