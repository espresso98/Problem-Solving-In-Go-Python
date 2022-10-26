# graph, DFS, O(m*n), O(m) where m is the number of equations
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i])) # append((nb, factor))
            graph[v].append((u, 1 / values[i]))
       
        res = []
        
        def bfs(u, v):
            if u not in graph or v not in graph:
                return -1.0
            
            queue = [(u, 1)]
            visited = set()
            
            for node, val in queue:
                if node == v:
                    return val
                visited.add(node)
                for nb, factor in graph[node]:
                    if nb not in visited:
                        queue.append((nb, val * factor))        
            
            return -1.0
        
        return [bfs(u, v) for u, v in queries]
                