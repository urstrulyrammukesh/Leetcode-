"""LeetCode 841. Keys and Rooms (Medium)
Approach: DFS from room 0 collecting keys; check every room was visited.
Time O(rooms + keys), space O(rooms).
"""


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        seen, stack = {0}, [0]
        while stack:
            for key in rooms[stack.pop()]:
                if key not in seen:
                    seen.add(key)
                    stack.append(key)
        return len(seen) == len(rooms)


if __name__ == "__main__":
    s = Solution()
    assert s.canVisitAllRooms([[1], [2], [3], []])
    assert not s.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]])
    print("lc841 ok")
