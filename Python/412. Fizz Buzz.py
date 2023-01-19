# O(N), O(1)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        divisibleByK = lambda n, k: n % k == 0
        res = []
        
        for num in range(1, n + 1):
            if divisibleByK(num,3) and divisibleByK(num,5):
                res.append("FizzBuzz")
            elif divisibleByK(num,3):
                res.append("Fizz")
            elif divisibleByK(num,5):
                res.append("Buzz")
            else: 
                res.append(str(num))
        return res
