# TC: O(NlogN), SC: O(1)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo, hi = max(weights), sum(weights)

        while lo < hi:
            cap = lo + (hi-lo) // 2   # mid: capacity
            cur_loads, num_days = 0, 1
            
            for new_load in weights:
                # print(cap, cur_loads, new_load, num_days)
                if cur_loads + new_load > cap:
                    num_days += 1
                    cur_loads = 0
                    
                cur_loads += new_load
            # print(cap, num_days)
            if num_days > days: 
                lo = cap + 1 # increase capacity 
            else:
                hi = cap
            # print("cap", lo, hi)
        return lo
        