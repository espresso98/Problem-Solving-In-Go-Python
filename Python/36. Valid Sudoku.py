# Hash Set. O(N^2), O(N^2)
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        
        for r in range(N):
            for c in range(N):
                if board[r][c] == ".":
                    continue
                    
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in boxes[(r // 3, c // 3)]
                ):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True
        