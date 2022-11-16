# TC & SC: O(n)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Solution 1
        freq = {}
        # freq[n] = freq.get(n, 0) + 1
        for n in arr:
            if n in freq:
                freq[n] += 1
            else: 
                freq[n] = 1
        return len(set(freq.values())) == len(set(arr))

        # Solution 2
        # import collections
        # freqs = collections.Counter(arr).values()
        freqs = {}
        for i in arr:
            freqs[i] = freqs.get(i, 0) + 1

        seen = set()
        for freq in freqs.values():
            if freq in seen:
                return False
            seen.add(freq)
        return True 