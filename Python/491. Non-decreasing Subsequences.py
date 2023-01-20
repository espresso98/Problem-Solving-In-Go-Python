# Backtrack: O(2^n*n), O(2^n*n)
# the subsequences/combinations/permutations of some group of letters/numbers => backtracking

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def backtrack(idx, cur):
            if idx == len(nums):
                if len(cur) >= 2:
                    res.add(tuple(cur))
                return
            # check non-decreasing
            if not cur or cur[-1] <= nums[idx]:
                cur.append(nums[idx])
                backtrack(idx + 1, cur)
                cur.pop()
            # call recursively not appending an element
            backtrack(idx + 1, cur)

        backtrack(0, [])
        return res
        