# O(N), O(N)
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i:[] for i in range(n)}
        # {0: [1, 2], 1: [0, 4, 5], 2: [0, 3, 6], 3: [2], 4: [1], 5: [1], 6: [2]}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(cur, parent=None):
            time = 0
            for child in adj[cur]:
                if child == parent:
                    continue
                child_time = dfs(child, cur) # cur -> parent 
                if hasApple[child] or child_time:
                    time += 2 + child_time
                # print(cur, child, child_time, hasApple[child], time)
            return time 
        
        return dfs(0) 
        