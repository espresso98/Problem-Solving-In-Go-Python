
# zip() iterates up to the length of the shortest iterator.
# zip_longest() iterates up to the length of the longest iterator.
# a word is always similar to itself. if w1 == w2, return true
# Time complexity: O((n+k)⋅m) = O(n+k) since m = 20
# O(len(sentence1) + len(sentence2) + len(similarPairs)) * (the average length of words in sentence1/2 and similarPairs)
# Space complexity: O(n)
from itertools import zip_longest
from typing import List
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        for w1, w2 in zip_longest(sentence1, sentence2):
            if w1 == w2 or [w1, w2] in similarPairs or [w2, w1] in similarPairs:
                continue
            else:
                return False
        return True

    # return all(a==b or [a,b] in similarPairs or [b,a] in similarPairs for a,b in itertools.zip_longest(sentence1,sentence2))
