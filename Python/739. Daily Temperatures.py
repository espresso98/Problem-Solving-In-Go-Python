# O(N), O(N)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        waits = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                cooler_day = stack.pop()
                waits[cooler_day] = day - cooler_day
            stack.append(day)
        return waits

 
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
