# Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

# O(1), O(1)
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bit_cnts(num):
            cnt = 0
            while num:
                cnt += num & 1
                num >>= 1
            return cnt

        return sorted(arr, key=lambda num: [bit_cnts(num), num])

        # return sorted(sorted(arr),key=lambda x:bin(x).count('1'))
        