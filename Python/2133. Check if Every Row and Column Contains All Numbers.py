# The * means that zip can take a variable number of iterables as arguments. 
# Thus, zip(*iterables) means zip(iterable1, iterable2, iterable3, ...).
from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix) 
        for row, col in zip(matrix, zip(*matrix)):
            if len(set(row)) != n or len(set(col)) != n:
                return False
        return True

class Solution2:    
    def checkValid(self, matrix: List[List[int]]) -> bool:   
        return all(len(set(x)) == len(matrix) for x in matrix + list(zip(*matrix)))

# matrix = [[1,2,3],[3,1,2],[2,3,1]]    
# print(list(zip(matrix, zip(*matrix))))
# [([1, 2, 3], (1, 3, 2)), ([3, 1, 2], (2, 1, 3)), ([2, 3, 1], (3, 2, 1))]
# print(list(zip(*matrix)))
# [(1, 3, 2), (2, 1, 3), (3, 2, 1)]