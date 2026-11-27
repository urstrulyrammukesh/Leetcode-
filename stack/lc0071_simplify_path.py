"""LeetCode 71. Simplify Path (Medium)
Approach: Split on '/', push folder names, pop on '..', ignore '.' and empty parts.
Time O(n), space O(n).
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part and part != ".":
                stack.append(part)
        return "/" + "/".join(stack)


if __name__ == "__main__":
    s = Solution()
    assert s.simplifyPath("/home/") == "/home"
    assert s.simplifyPath("/../") == "/"
    assert s.simplifyPath("/home//foo/") == "/home/foo"
    assert s.simplifyPath("/a/./b/../../c/") == "/c"
    print("lc71 ok")
