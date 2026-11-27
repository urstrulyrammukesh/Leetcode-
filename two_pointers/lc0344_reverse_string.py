"""LeetCode 344. Reverse String (Easy)
Approach: Swap the two ends and move both pointers inward.
Time O(n), space O(1).
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1


if __name__ == "__main__":
    s = Solution()
    a = list("hello")
    s.reverseString(a)
    assert a == list("olleh")
    b = list("Hannah")
    s.reverseString(b)
    assert b == list("hannaH")
    print("lc344 ok")
