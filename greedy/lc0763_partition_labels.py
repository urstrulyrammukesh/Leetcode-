"""LeetCode 763. Partition Labels (Medium)
Approach: Know each letter's last index; close a part when the scan reaches the furthest last index seen.
Time O(n), space O(1).
"""


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        out, start, end = [], 0, 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                out.append(end - start + 1)
                start = i + 1
        return out


if __name__ == "__main__":
    s = Solution()
    assert s.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert s.partitionLabels("eccbbbbdec") == [10]
    print("lc763 ok")
