# TC: O(nm), SC: O(1)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        for j in range(len(strs[0])): # column
            for i in range(len(strs)-1): # row
                if strs[i][j] > strs[i+1][j]:
                    delete += 1
                    break
        return delete
        