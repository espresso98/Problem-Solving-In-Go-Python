#  O(n) / O(n)
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums = [lower-1] + nums + [upper + 1]

        for i in range(1, len(nums)):
            start = nums[i-1] + 1
            end  = nums[i] - 1
            if start == end:
                res.append(str(end))
            elif start < end:
                res.append(f"{start}->{end}")
                
        return res


class Solution2:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        nums_ext = [lower-1] + nums + [upper + 1]

        for i in range(len(nums_ext) - 1):
            if nums_ext[i+1] - nums_ext[i] == 2:
                res.append(f"{nums_ext[i] + 1}")
            elif nums_ext[i+1] - nums_ext[i] > 2:             
                res.append(f"{nums_ext[i] + 1}->{nums_ext[i+1] - 1}")   
        return res 
