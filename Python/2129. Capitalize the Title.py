class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.lower().split()
        print(words)
        for i, word in enumerate(words):
            if len(word) > 2:
                words[i] = word[0].upper() + word[1:]
        capitalized = " ".join(words)
        return capitalized
        