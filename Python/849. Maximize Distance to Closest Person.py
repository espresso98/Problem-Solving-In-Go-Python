# seats[i] = 1 represents a person sitting in the ith seat
# seats[i] = 0 represents that the ith seat is empty
# Return that maximum distance to the closest person

# TC: O(n), SC: O(1)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = -1     # idx for prev taken seat from left
        max_dist = 0
        
        for cur in range(len(seats)):
            if seats[cur] == 1:
                if prev == -1:
                    max_dist = cur
                else: 
                    max_dist = max(max_dist, (cur - prev) // 2)      
                prev = cur   
      
        # [1,0,0,1,0,0,0,0]        
        if seats[-1] == 0:   # check the dist from right
            max_dist = max(max_dist, cur - prev)  # len(seats)-1-prev
            
        return max_dist