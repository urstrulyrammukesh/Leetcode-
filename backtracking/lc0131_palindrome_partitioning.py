"""LeetCode 131. Palindrome Partitioning (Medium)
Approach: Cut off every palindromic prefix and partition the rest recursively.
Time O(n * 2^n), space O(n).
"""


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        out, path = [], []

        def go(i):
            if i == len(s):
                out.append(path[:])
                return
            for j in range(i + 1, len(s) + 1):
                part = s[i:j]
                if part == part[::-1]:
                    path.append(part)
                    go(j)
                    path.pop()

        go(0)
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.partition("aab") == [["a", "a", "b"], ["aa", "b"]]
    assert s.partition("a") == [["a"]]
    print("lc131 ok")
