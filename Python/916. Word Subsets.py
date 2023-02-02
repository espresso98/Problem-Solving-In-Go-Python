# A string b is a subset of string a if every letter in b occurs in a including multiplicity.("wrr" is a subset of "warrior")
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# O(M+N), O(1)
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            cnts = [0] * 26
            for ch in word:
                cnts[ord(ch) - ord('a')] += 1
            return cnts

       # subset max counts
        words2_max = [0] * 26
        for w2 in words2: 
            for i, cnt in enumerate(count(w2)):
                words2_max[i] = max(words2_max[i], cnt)  # merge subsets' counts
       
        res = []
        for w1 in words1:
            # universal if for every string w2 in words2, w2 is a subset of w1
            if all(w1_cnt >= w2_cnt for w1_cnt, w2_cnt in zip(count(w1), words2_max)):
                res.append(w1) # universal strings in words1
        return res
      
