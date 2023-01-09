# All the points are unique.

from typing import List
from collections import Counter

# O(N^2), O(N): More accurate solution 
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2: return n
  
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def slope(dx, dy):
            gcds = gcd(dx, dy)
            return (dx // gcds, dy // gcds)

        points = list(map(tuple, points))   # [(1, 1), (3, 2), (5, 3), (4, 1), (2, 3), (1, 4)]
        res = 0
        for i in range(n):
            slope_cnts = Counter()   # {(2, 1): 2, (1, 0): 1, (1, 2): 1, (0, 1): 1}
            for j in range(i + 1, n):
                # for each pair of (x1, y1) and (x2, y2), compute slope as (dx // gcd, dy // gcd)
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx, dy = x2 - x1, y2 - y1    # 2 1 (2, 1)/ 4 2 (2, 1)/ 3 0 (1, 0)/ 1 2 (1, 2)/ 0 3 (0, 1)
                slope_cnts[slope(dx, dy)] += 1  # points[j]
            if slope_cnts:
                res = max(res, max(slope_cnts.values()) + 1)  # points[i]

        return res 


# O(N^2), O(N)
class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0 
        for i, (x0,y0) in enumerate(points[:-1]):
            slope_cnts = Counter(((x-x0)/(y-y0) if (y-y0) != 0 else inf) for x,y in points[i+1:])
            # Counter({2.0: 2, inf: 1, 0.5: 1, 0.0: 1}) inf: y=y0, 0.0: x=x0
            res = max(res, max(slope_cnts.values()))
        return res + 1

# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
