def is_valid(s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for c in s:
        if c in pairs.values():          # opening
            stack.append(c)
        elif c in pairs:                 # closing
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()

    return not stack