# O(r*c)^2, O(r*c)
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        M, N, B = len(board), len(board[0]), board

        while True:
            crush = set()
            # step1: detect candies to crush
            for r in range(M):
                for c in range(N):
                    # If three or more candies of the same type are adjacent
                    if c >= 2 and B[r][c] and B[r][c] == B[r][c-1] == B[r][c-2]: # horizontally
                        crush = crush.union({(r,c),(r,c-1),(r,c-2)})
                    if r >= 2 and B[r][c] and B[r][c] == B[r-1][c] == B[r-2][c]: # vertically
                        crush = crush.union({(r,c),(r-1,c),(r-2,c)})            
            # print(crush)
            # {(6, 2), (7, 1), (8, 4), (8, 1), (6, 1), (8, 3), (7, 2), (8, 2), (9, 1)}
            # {(9, 0), (4, 0), (8, 4), (9, 3), (4, 3), (8, 1), (5, 4), (9, 2), (4, 2), 
            #  (8, 0), (8, 3), (5, 3), (8, 2), (9, 1), (4, 1), (5, 2)}
            # step2: crush candies => update cells to 0(empty)
            if not crush:
                break
            for r, c in crush:
                B[r][c] = 0
            # step3: gravity => drop non-empty cells
            for c in range(N):
                non_zeroes = M-1
                for r in reversed(range(M)):
                    if B[r][c] != 0:
                        B[non_zeroes][c] = B[r][c]
                        non_zeroes -= 1        
                for row in range(non_zeroes + 1):
                    B[row][c] = 0
                    
        return B  
