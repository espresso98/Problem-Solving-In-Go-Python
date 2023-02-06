# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "". wildcard
# Greedy: O(N), O(1)
class Solution(object):
    def checkValidString(self, s):
        lmin, lmax = 0, 0  # the smallest and largest possible number of open left brackets
        for ch in s:
            lmin += 1 if ch == "(" else -1               # +1 for "(",       -1 for ")", "*"
            lmax += 1 if ch == "(" or ch == "*" else -1  # +1 for "(", "*",  -1 for ")" 
            # lmax += 1 if ch != ")" else -1               
            if lmax < 0: return False
            lmin = max(lmin, 0) # we can never have less than 0 open left brackets
        return lmin == 0  # valid


# class Solution2:
#     def checkValidString(self, s: str) -> bool:
#         lmin, lmax = 0, 0  # the smallest and largest possible number of open left brackets
#         for ch in s:
#             if ch == "(":
#                 lmin += 1
#                 lmax += 1   
#             elif ch == ")":
#                 lmin -= 1
#                 lmax -= 1
#             else:  # "*": wildcard 
#                 lmin -= 1
#                 lmax += 1
            
#             if lmax < 0:  # invalid
#                 return False
#             lmin = max(lmin, 0)
#         return lmin == 0
