def hammingWeight(self, n: int) -> int:
    # Solution1: O(32) in time, O(1) in space
    cnt = 0
    while n:
        cnt += n & 1
        n >>= 1
    return cnt
    
        
    # Solution2: O(K) where K is number of 1-bits, O(1)
    # n & (n-1) always flips the least significant 1-bit in n to 0, and keeps all other bits the same.
    # n & (n-1): 1011 -> 1010 -> 1000 -> 0000
    cnt = 0
    while n:
        cnt += 1
        n &= (n-1)  
    return cnt