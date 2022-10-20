# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down)
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 0, 1, 6->9, 8, 9->6
# num = "69", num = "88" -> True
# num = "962" -> False
# num = "6" -> False
# TC: O(N), SC: O(1)

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        l, r = 0, len(num)-1
        while l <= r:
            if num[l] not in rotated_digits or num[r] not in rotated_digits:
                return False
            elif num[l] != rotated_digits[num[r]]: # 6 != 9
                return False
            l, r = l+1, r-1
        return True