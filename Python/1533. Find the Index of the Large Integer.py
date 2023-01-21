# We have an integer array arr, where all the integers in arr are equal except for one integer which is larger than the rest of the integers. 
# Return the index of the array arr which has the largest integer.
cclass Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l, r = 0, reader.length() - 1
        while l < r:
            mid = l + (r - l) // 2
            if (r - l + 1) % 2 == 0:  # even
                res = reader.compareSub(l, mid, mid+1, r)    # 0-4, 5-8
                if res == -1:           
                    l = mid + 1    
                else: 
                    r = mid  
            else:                     # odd              
                res = reader.compareSub(l, mid-1, mid+1, r)  # 0-3, 5-7 
                if res == 0:
                    return mid
                elif res == -1:
                    l = mid +1
                elif res == 1:
                    r = mid - 1
                
        return l
        