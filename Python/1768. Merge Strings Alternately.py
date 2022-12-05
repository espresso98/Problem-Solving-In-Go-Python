class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(min(len(word1), len(word2))):
            res += word1[i] + word2[i]
            print(i)
        return res + word1[i+1:] + word2[i+1:]

from itertools import zip_longest       
class Solution2:
    def mergeAlternately(self, word1: str, word2: str) -> str:        
        return ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
