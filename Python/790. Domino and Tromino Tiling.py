# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 10^9 + 7
# f[k]: number of ways to "fully cover a board" of width k
# full(k) = full(k-1) + full(k-2) + part(k-1) * 2 
# p[k]: number of ways to "partially cover a board" of width k
# part(k) = full(k-2) + part(k-1)

# DP, Bottom-up: O(N), O(N)
class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n <= 2: return n
        f = [0] * (n+1) 
        p = [0] * (n+1)

        f[1], f[2], p[2] = 1, 2, 1
        for k in range(3, n+1):
            f[k] = (f[k-1] + f[k-2] + 2 * p[k-1]) % MOD
            p[k] = (f[k-2] + p[k-1]) % MOD
        return f[n]

# DP, Bottom-up: O(N), O(1)
class Solution2:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        if n <= 2: return n
       
        f_prev, f_cur, p_cur = 1, 2, 1
        for k in range(3, n+1):
            tmp = f_cur
            f_cur = (f_cur + f_prev + 2*p_cur) % MOD
            p_cur = (f_prev + p_cur) % MOD
            f_prev = tmp
        return f_cur


# DP, Top-down: O(N), O(N)
# class Solution:
#     def numTilings(self, n: int) -> int:
#         MOD = 10**9 + 7
#         @cache
#         def full(k):
#             if k == 1: return 1
#             if k == 2: return 2
#             return (full(k-1) + full(k-2) + 2 * part(k-1)) % MOD
        
#         @cache
#         def part(k):
#             if k == 2: return 1
#             return (full(k-2) + part(k-1)) % MOD
        
#         return full(n)