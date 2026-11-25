"""Valid Parentheses: check brackets are balanced and correctly nested. O(n) with a stack."""

def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack

if __name__ == "__main__":
    assert is_valid("()[]{}")
    assert is_valid("{[()]}")
    assert not is_valid("(]")
    assert not is_valid("((")
    print("p02 ok")
