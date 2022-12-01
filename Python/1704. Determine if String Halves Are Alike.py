def halvesAreAlike(self, s: str) -> bool:
    first, second = s[:len(s)//2], s[len(s)//2:]
    return sum(ch.lower() in 'aeiou' for ch in first) == sum(ch.lower() in 'aeiou' for ch in second)
