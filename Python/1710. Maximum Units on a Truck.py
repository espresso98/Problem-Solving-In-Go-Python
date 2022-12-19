# O(NlogN), O(1)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        sorted_box = sorted(boxTypes, key=lambda x: x[1], reverse=True)

        for num_box, unit in sorted_box:
            if num_box <= truckSize:
                res += num_box * unit
                truckSize -= num_box
                if truckSize == 0: 
                    break
            elif num_box > truckSize:
                res += truckSize * unit
                truckSize = 0
                break
        return res
        