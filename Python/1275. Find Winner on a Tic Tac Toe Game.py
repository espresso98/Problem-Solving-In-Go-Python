# Let n be the length of the board and m be the length of input moves.
# Time complexity : O(m) / Space complexity: O(n) where m be the length of input moves

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag, anti_diag = 0, 0
        player = 1  # 'A'
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c: 
                diag += player
            if r + c == n-1:
                anti_diag += player
            if any(abs(score) == n for score in (rows[r], cols[c], diag, anti_diag)):
                return "A" if player == 1 else "B"
            player *= -1 # switch a turn
            
        return "Draw" if len(moves) == n * n else "Pending"
