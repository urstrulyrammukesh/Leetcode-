"""LeetCode 380. Insert Delete GetRandom O(1) (Medium)
Approach: A list for random picks plus a map value -> index; delete by swapping with the last element.
Time O(1) average per operation, space O(n).
"""
import random


class RandomizedSet:
    def __init__(self):
        self.vals, self.pos = [], {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        i, last = self.pos[val], self.vals[-1]
        self.vals[i], self.pos[last] = last, i
        self.vals.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


if __name__ == "__main__":
    r = RandomizedSet()
    assert r.insert(1) and not r.remove(2) and r.insert(2)
    assert r.getRandom() in (1, 2)
    assert r.remove(1) and not r.insert(2)
    assert r.getRandom() == 2
    print("lc380 ok")
