"""LeetCode 17. Letter Combinations of a Phone Number (Medium)
Approach: Build combinations digit by digit (iterative product over the phone letters).
Time O(4^n * n), space O(4^n).
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        pad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []
        out = [""]
        for d in digits:
            out = [p + c for p in out for c in pad[d]]
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert s.letterCombinations("") == []
    assert s.letterCombinations("2") == ["a", "b", "c"]
    print("lc17 ok")
