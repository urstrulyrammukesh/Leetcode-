"""LeetCode 621. Task Scheduler (Medium)
Approach: Formula: the most frequent task sets (maxCount - 1) frames of length n + 1, plus the tasks tied for the max.
Time O(n), space O(1).
"""
from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks).values()
        top = max(counts)
        ties = sum(1 for c in counts if c == top)
        return max(len(tasks), (top - 1) * (n + 1) + ties)


if __name__ == "__main__":
    s = Solution()
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert s.leastInterval(["A", "C", "A", "B", "D", "B"], 1) == 6
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 3) == 10
    print("lc621 ok")
