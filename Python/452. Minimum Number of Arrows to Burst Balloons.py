# O(NlogN), O(N)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points: 
            return 0

        points.sort(key=lambda x: x[1])
        res = 1
        prev_end = points[0][1]
        
        for i in range(1, len(points)):
            start, end = points[i][0], points[i][1]
            if start > prev_end: 
                # needs one more arrow if the current balloon starts after the end of another one
                res += 1
                prev_end = end 
        return res
