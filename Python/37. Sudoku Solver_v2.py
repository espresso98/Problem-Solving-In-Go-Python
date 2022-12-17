# O((9!)^9), O(9^2)
from collections import defaultdict
from typing import List

def solveSudoku(self, board: List[List[str]]) -> None:
        N = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        def is_valid(r, c, d):
            return d not in rows[r] and d not in cols[c] and d not in boxes[(r//3, c//3)]

        def place_candidate(d, r, c):
            rows[r].add(d)
            cols[c].add(d)
            boxes[(r//3, c//3)].add(d)
            board[r][c] = d

        def remove_candidate(d, r, c):
            rows[r].remove(d)
            cols[c].remove(d)
            boxes[(r//3, c//3)].remove(d)
            board[r][c] = "."

        def backtrack(r = 0, c = 0):
            if r == N:
                self.sudoku_solved = True
                return
            else:
                if c == N - 1:
                    next_r, next_c = r + 1, 0
                else: 
                    next_r, next_c = r, c + 1

            if board[r][c] == '.':
                for d in range(1, 10):
                    d = str(d)
                    if is_valid(r, c, d):
                        place_candidate(d, r, c)
                        backtrack(next_r, next_c)  
                        if not self.sudoku_solved:
                            remove_candidate(d, r, c)
            else: 
                backtrack(next_r, next_c)

        for r in range(N):
            for c in range(N):
                if board[r][c] != ".":
                    d = board[r][c]
                    place_candidate(d, r, c)

        self.sudoku_solved = False
        backtrack()
             