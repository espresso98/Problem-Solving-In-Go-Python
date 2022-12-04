from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cnts = Counter(s)
        res = []
        for ch, freq in sorted(cnts.items(), key=lambda x:x[1], reverse=True):
            res.append(ch * freq)
        return ''.join(res)
      