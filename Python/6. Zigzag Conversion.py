# PAYPALISHIRING, numRows = 3: write in a zigzag pattern on a given number of rows
# P   A   H    N
# A P L S I  I G
# Y   I   R
# O(N*M), O(N*M) where n is the length of the input string and m is the numRows
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): 
            return s
        rows = [[] for _ in range(numRows)]
        i = step = 0
        for ch in s:     # O(N)      
            rows[i].append(ch)
            if i == 0:    # first row
                step = 1  # down
            if i == numRows - 1:  # last row
                step = -1  # up
            # print(ch, i, step, rows)
            i += step    
        return ''.join(''.join(row) for row in rows)
                 