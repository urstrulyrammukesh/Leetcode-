"""LeetCode 394. Decode String (Medium)
Approach: On '[' push the current text and repeat count; on ']' pop and repeat the inner text.
Time O(output), space O(output).
"""


class Solution:
    def decodeString(self, s: str) -> str:
        stack, cur, num = [], "", 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((cur, num))
                cur, num = "", 0
            elif c == "]":
                prev, k = stack.pop()
                cur = prev + cur * k
            else:
                cur += c
        return cur


if __name__ == "__main__":
    s = Solution()
    assert s.decodeString("3[a]2[bc]") == "aaabcbc"
    assert s.decodeString("3[a2[c]]") == "accaccacc"
    assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    print("lc394 ok")
