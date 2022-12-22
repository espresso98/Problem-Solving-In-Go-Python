# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.
# ans[y] = x@X + y@Y + #(X)
# O(N), O(N) where N is the number of nodes in the graph
from collections import defaultdict
from typing import List

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
       # {0: {1, 2}, 1: {0}, 2: {0, 3, 4, 5}, 3: {2}, 4: {2}, 5: {2}})

        sum_dist = [0] * n    
        subtree_cnt = [1] * n  

        # 1. postorder: bottom up from leaf node, complete a subtree_cnt list and cacluate a sum_dist from a leaf nodes
        def postorder(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    postorder(child, node)
                    subtree_cnt[node] += subtree_cnt[child]
                    sum_dist[node] += sum_dist[child] + subtree_cnt[child]

                # subtree_cnt [6, 1, 4, 1, 1, 1]
                # sum_dist [8, 0, 3, 0, 0, 0]

        # 2. preorder: top down from root, parent -> child, cacluate a sum_dist on a each child
        def preorder(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    sum_dist[child] = (sum_dist[node] - subtree_cnt[child]) + (n - subtree_cnt[child])
                    # sum_dist [8, 12, 6, 10, 10, 10]
                    preorder(child, node)

        postorder()
        preorder()
        return sum_dist 
