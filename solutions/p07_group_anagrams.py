"""Group Anagrams: group words that are anagrams of each other. O(n * k log k)."""
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)
    return list(groups.values())

if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, result)) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    print("p07 ok")
