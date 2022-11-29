# Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
import math
from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist, idx = math.inf, -1
        for i, (r, c) in enumerate(points):
            if r == x or c == y:
                cur_dist = abs(x - r) + abs(y - c)
                if cur_dist < min_dist:
                    min_dist, idx = cur_dist, i
        return idx
            