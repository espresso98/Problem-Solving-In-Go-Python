# O(1), O(1)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        # u, v = edges[1]
        # return u if u in edges[0] else v

        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

        # return (set(edges[0]) & set(edges[1])).pop()
        

"""
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: node 2 is connected to every other node, so 2 is the center.
"""
