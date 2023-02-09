# Detect Cycles with a HashSet
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(d)**2 for d in str(n)])
            if n == 1:
                return True
        return False

        # def SquareOfNumbers(a):
        #     Sum = 0
        #     while a > 0:
        #         digit = a%10
        #         Sum+=(digit*digit)
        #         a = a//10
        #     return Sum
        
class Solution2:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                # n, digit = divmod(n, 10)
                n, digit = n // 10, n % 10
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n) # 82, 68, 100, 1

        return n == 1
        