class Solution: 
    # Solution 1: O(nlogn) / O(n), split-sort-join
    def sortSentence(self, s: str) -> str:
        words = sorted(s.split(), key=lambda w: w[-1])
        res = [word[:-1] for word in words]
        return " ".join(res)
        
        # one line
        return ' '.join(x for _, x in sorted((w[-1], w[:-1]) for w in s.split()))
    
    
    # Solution 2: O(n) / O(n)    
    def sortSentence(self, s: str) -> str:    
        words = s.split()
        res = [None] * len(words)
        
        # ['is2', 'sentence4', 'This1', 'a3']
        for word in words:
            idx = int(word[-1])
            res[idx-1] = word[:-1]

        return ' '.join(res)

# Input: s = "is2 sentence4 This1 a3"
# Output: "This is a sentence"
# Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.
