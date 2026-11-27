"""LeetCode 733. Flood Fill (Easy)
Approach: DFS from the start pixel, recolouring every connected pixel of the old colour.
Time O(m * n), space O(m * n).
"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        old = image[sr][sc]
        if old == color:
            return image
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == old:
                image[r][c] = color
                stack += [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
        return image


if __name__ == "__main__":
    s = Solution()
    assert s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
    assert s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]
    print("lc733 ok")
