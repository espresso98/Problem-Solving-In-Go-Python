class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(target, curr, start):
            if target == 0:
                result.append(curr.copy())
            elif target < 0:
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    curr.append(candidates[i])
                    dfs(target - candidates[i], curr, i)
                    curr.pop()
        
        dfs(target, [], 0)
        return result
        
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
