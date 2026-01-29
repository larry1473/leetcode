def countVowels(string: str) -> int:
    """" Counts the number of vowels in a given string."""
    return sum( 1 for c in string.lower() if c in "aeiou")