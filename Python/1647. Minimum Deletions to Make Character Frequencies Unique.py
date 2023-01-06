# Given a string s, return the minimum number of characters you need to delete to make s good.
# Counter + sort list + set
# O(n + k log k), O(k) -  k : unique frequencies
class Solution:
    def minDeletions(self, s: str) -> int:               # s: "ceabaacb"
        freqs = list(collections.Counter(s).values())    # Counter({'a': 3, 'c': 2, 'b': 2, 'e': 1})
        freqs.sort(reverse=True)                         # freqs: [3, 2, 2, 1]
        seen = set()
        delete = 0
        for val in freqs:
            while val in seen and val > 0:
                val -= 1  
                delete += 1
            seen.add(val)
        return delete


 class Solution2:
    def minDeletions(self, s: str) -> int:        
        # O(n + k^2), O(k)
        freqs = collections.Counter(s) 
        dels = 0
        seen = set()                   
 
        for ch, freq in freqs.items():
            while freq in seen and freq > 0:
                freq -= 1
                dels += 1
            seen.add(freq)
        
        return dels
        