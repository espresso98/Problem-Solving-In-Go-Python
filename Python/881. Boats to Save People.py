# Time complexity: O(NlogN)
# Space complexity: O(N) for soting
# two pointer and greedy
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        p = sorted(people)
        lo, hi = 0, len(p)-1
        cnt = 0
        
        while lo <= hi:
            cnt += 1
            if p[lo] + p[hi] <= limit:
                lo += 1
            hi -= 1  
        return cnt
        