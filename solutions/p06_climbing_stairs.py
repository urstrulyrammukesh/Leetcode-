"""Climbing Stairs: ways to climb n steps taking 1 or 2 at a time (dynamic programming). O(n)."""

def climb_stairs(n):
    a, b = 1, 1
    for _ in range(n):
        a, b = b, a + b
    return a

if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(5) == 8
    print("p06 ok")
