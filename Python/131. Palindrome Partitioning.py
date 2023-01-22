# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# Backtracking: O(2^N*N), O(N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def backtrack(start, cur_list):
            if start == len(s): 
                res.append(list(cur_list))  # cur_list.copy()
                return

            for end in range(start, len(s)):
                # print(start, end, s[start:end+1], s[start:end+1][::-1])
                if s[start:end+1] == s[start:end+1][::-1]: 
                    cur_list.append(s[start:end+1])
                    backtrack(end+1, cur_list) 
                    cur_list.pop()

        backtrack(0,[])
        return res

# BFS
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
      res = []
        def dfs(i, path):
            if i == len(s): 
                res.append(path)
                return

            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:    
                    dfs(j+1, path + [s[i:j+1]]) 

        dfs(0,[])
        return res  
        
# Backtracking
class Solution3:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(l, r, s):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r -1
            return True

        def backtrack(i, path):
            if i == len(s): 
                res.append(path.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j, s):
                    path.append(s[i:j+1])
                    backtrack(j+1, path)
                    path.pop()

        backtrack(0,[])
        return res
