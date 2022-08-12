# TC: O(N), SC: O(1)
class Solution:
    def compress(self, chs: List[str]) -> int:
        i = 0
        cnt = 1
        for j in range(1, len(chs)+1):
            if j < len(chs) and chs[j] == chs[j-1]:
                cnt += 1
            else:
                chs[i] = chs[j-1]
                i += 1
                if cnt > 1:
                    for k in str(cnt):
                        chs[i] = k
                        i += 1
                cnt = 1
                
        chs = chs[:i]
        return i

                        
# Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
# Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".