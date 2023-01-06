# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
# Note that after rotating a number, we can ignore leading zeros.
# TC: O(L) where L is the maximum number of digits n can have (L=log(10)N), SC: O(1)
class Solution:
    def confusingNumber(self, n: int) -> bool:
        digits = str(n)
        candidate = ""
        invert = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        for i in range(len(digits)-1, -1, -1): # n = 916, reverse = 619  # n = 89, reverse = 98
            if digits[i] not in invert:
                return False
            candidate += invert[digits[i]]     # 9(<-6) + 1 + 6(<-9)     # 6(<-9) + 8
        return candidate != str(n)             # cand = 916, n = 916     # True  68 != 89
        