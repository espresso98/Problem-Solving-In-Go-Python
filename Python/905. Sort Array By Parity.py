def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Soultion 1: O(n), O(1)
        if len(nums) <= 1: return nums
        i, j, N = 0, len(nums)-1, nums
        
        while i < j:
            if N[i] % 2 > N[j] % 2: 
                N[i], N[j] = N[j], N[i]
            if N[i] % 2 == 0: i += 1
            if N[j] % 2 == 1: j -= 1
        return N
    
        # Soultion 2: O(nlogn), O(n)
        return sorted(nums, key=lambda n: n % 2)
    
        # Soultion 3: O(n), O(n)
        even = [n for n in nums if n % 2 == 0]
        odd = [n for n in nums if n % 2 == 1]
        return even + odd
        