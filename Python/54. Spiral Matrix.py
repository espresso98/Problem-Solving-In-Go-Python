# O(M*N) / O(1) if the output array is not taken into account
# Layer-by-layer

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix)-1
        left, right = 0, len(matrix[0])-1 
        
        while top <= bottom and left <= right:
            # start at top-left and move right
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1 # shift boundary, row down by 1
            
            # move down to bottom-right
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            # [1,2,3] row matrix or column matrix [1,
            #                                      2]
            # top > bottom: row matrix, left > right: column matrix
            if top > bottom or left > right: 
                break
            # move left to bottom-left when top <= bottom:
            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            # move up to top-left when left <= right:
            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1
                
        return res
                