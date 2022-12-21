# O(1), O(N)
import random
class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        
    def insert(self, val: int) -> bool:
        res = val not in self.numMap
        if res:
            self.numList.append(val)
            self.numMap[val] = len(self.numList)-1
        return res
        
    
    def remove(self, val: int) -> bool:
        res = val in self.numMap
        if res:
            # move last value into removed element's place
            idx = self.numMap[val]
            last = self.numList[-1]
            self.numList[idx] = last
            self.numList.pop()
            self.numMap[last] = idx
            del self.numMap[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
