class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # dy    y1 - y0      y - y1
        # -- =  -------  =   --------
        # dx    x1 - x0       x - x1 
    
        if len(coordinates) == 2: return True
        (x0, y0), (x1, y1) = coordinates[:2]
        dx, dy = x1 - x0, y1 - y0
        # dy / dx = (y - y1) / (x - x1)
        return all(dx * (y - y1) == dy * (x - x1) for x, y in coordinates)
        