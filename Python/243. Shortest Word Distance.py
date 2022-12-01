class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortest = math.inf
        w1, w2 = -1, -1
        for idx, word in enumerate(wordsDict):
            if word == word1:
                w1 = idx
            elif word == word2:
                w2 = idx
            if w1 != -1 and w2 != -1:
                shortest = min(shortest, abs(w1 - w2))
        return shortest
        