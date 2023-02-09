# return the earliest time slot that works for both of them and is of duration duration
# Two pointer: O(nlogn + mlogm), O(n+m)
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        valid = lambda time: time[1] - time[0] >= duration
        vs1, vs2 = list(filter(valid, slots1)), list(filter(valid, slots2))
        # sort both by the start time
        s1, s2 = sorted(vs1), sorted(vs2)

        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            # find intersection which is greater than or equal to duration
            start = max(s1[i][0], s2[j][0])  
            end = min(s1[i][1], s2[j][1])   
            if end - start >= duration:
                return [start, start + duration]
            # move the one that ends earlier  
            if s1[i][1] < s2[j][1]: 
                i += 1
            else:       
                j += 1
        return []
