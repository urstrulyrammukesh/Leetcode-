"""LeetCode 496. Next Greater Element I (Easy)
Approach: Monotonic decreasing stack over nums2 gives every number's next greater element in one pass.
Time O(n + m), space O(n).
"""


class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nxt, stack = {}, []
        for x in nums2:
            while stack and stack[-1] < x:
                nxt[stack.pop()] = x
            stack.append(x)
        return [nxt.get(x, -1) for x in nums1]


if __name__ == "__main__":
    s = Solution()
    assert s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert s.nextGreaterElement([2, 4], [1, 2, 3, 4]) == [3, -1]
    print("lc496 ok")
