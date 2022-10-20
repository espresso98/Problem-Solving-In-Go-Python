# TC: O(N), SC: O(1)    
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = []    
        seed_chars = set(words[0])  
        for ch in seed_chars: 
            freqs = [word.count(ch) for word in words]
            min_freq = min(freqs)
            if min_freq > 0:
                common_chars.extend(ch * min_freq)
        return common_chars

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]