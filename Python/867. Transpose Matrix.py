# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
# O(MN), O(1)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:  
        # Solution1
        M, R, C = matrix, len(matrix), len(matrix[0])
        res = [] 
        for c in range(C):
            row = []
            for r in range(R):
                row.append(M[r][c])
            res.append(row)
        return res
                
        # Solution2    
        M, R, C = matrix, len(matrix), len(matrix[0])
        return [[M[r][c] for r in range(R)] for c in range(C)]

# Input: matrix = [[1,2,3],[4,5,6]]
# Output: [[1,4],[2,5],[3,6]]