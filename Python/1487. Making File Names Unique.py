# O(N), O(N)
from collections import defaultdict
from typing import List

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        assigned = defaultdict(int)  # {folder: last used index}
        res = []   
        for name in names:
            if name not in assigned:
                assigned[name] = 1
                res.append(name)
            else:       # reserved
                k = assigned[name]            # 'gta': 1 
                new_name = name               # 'gta(1)'
                while new_name in assigned:
                    k += 1
                    new_name = f"{name}({k})" # 'gta(2)'
                assigned[name] = k            # 'gta': 2 <- last used index
                assigned[new_name] = 1
                res.append(new_name)  
        return res

# Input: names = ["gta","gta(1)","gta","avalon"]
# Output: ["gta","gta(1)","gta(2)","avalon"]
# {'gta': 2, 'gta(1)': 1, 'gta(2)': 1, 'avalon': 1}
