# Write a program to solve a Sudoku puzzle by filling the empty cells.
# O((9!)^9), O(9^2)
from collections import defaultdict
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        N = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        to_visit = []

        for r in range(N):
            for c in range(N):
                if board[r][c] != ".":
                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    boxes[(r//3, c//3)].add(board[r][c])
                else:
                    to_visit.append((r, c))

        def is_valid(r, c, v):
            return v not in rows[r] and v not in cols[c] and v not in boxes[(r//3, c//3)]

        def backtrack():
            if not to_visit:
                return True

            r, c = to_visit.pop()

            for v in range(1, N + 1):
                val = str(v)  # candidate
                if is_valid(r, c, val):
                    # place
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3, c//3)].add(val)

                    if backtrack():
                        return True
                    # remove
                    board[r][c] = "."
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[(r//3, c//3)].remove(val)

            to_visit.append((r, c))
            return False

        backtrack()
