# TC: O(N), SC: O(26) -> O(1)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIdx = { ch: idx for idx, ch in enumerate(order) }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            for j in range(len(w1)): 
                if j == len(w2): # in case w2 is the prefix of w1
                    return False # False if the second string is shorter in size
                if w1[j] != w2[j]: # look for the first different char
                    if orderIdx[w1[j]] > orderIdx[w2[j]]: # verify the order
                        return False
                    else: break  # verified
        return True

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true