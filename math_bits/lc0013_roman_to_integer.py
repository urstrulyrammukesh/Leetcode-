"""LeetCode 13. Roman to Integer (Easy)
Approach: Add each symbol, but subtract it when a bigger symbol follows (like IV or XC).
Time O(n), space O(1).
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        v = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        for a, b in zip(s, s[1:] + " "):
            total += -v[a] if b != " " and v[a] < v[b] else v[a]
        return total


if __name__ == "__main__":
    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    print("lc13 ok")
