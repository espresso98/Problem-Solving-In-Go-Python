# O(N), O(M) 
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        chars, words = list(pattern), s.split(' ')
        if (len(chars) != len(words)) or (len(set(chars)) != len(set(words))):
            return False

        hm = dict()
        for i in range(len(chars)):
            ch, word = chars[i], words[i]  
            if (ch in hm) and (hm[ch] != word):
                return False
            hm[ch] = word
        return True
