# O(NlogN), O(N)
from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []

        changed.sort()
        num_map = Counter(changed)
        # changed = [1,3,4,2,6,8] 
        # num_map = {1: 1, 2: 1, 3: 1, 4: 1, 6: 1, 8: 1}
        res = []

        for num in num_map:
            double = num * 2
            if num_map[num] > 0:               
                if double in num_map and num_map[num] <= num_map[double]:
                    if num == 0:
                        count = num_map[num] // 2
                    else:
                        count = num_map[num]
                        
                    res.extend([num] * count)
                    num_map[num] -= count
                    num_map[double] -= count
                else:
                    return []
        
        return res

# 2 Counter({3: 1, 4: 1, 6: 1, 8: 1, 1: 0, 2: 0})
# 6 Counter({4: 1, 8: 1, 1: 0, 2: 0, 3: 0, 6: 0})
# 8 Counter({1: 0, 2: 0, 3: 0, 4: 0, 6: 0, 8: 0})

# [1,2,1,0]
# []