from collections import Counter
def first_non_repeating_char(s:str) -> str:
    counts = Counter(s)
    for c in s:
        if counts[c] == 1:
            return c
    return "_"