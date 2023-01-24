# O(N^2), O(N^2)
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        board.reverse() # [[-1, 15, -1, -1, -1, -1],...]
        def num_to_position(num):
            r = (num - 1) // N
            c = (num - 1) % N
            if r % 2:          # odd idx row
                c = N - 1 - c  # flip
            return (r,c)       # 1 -> (0,0) 7 -> (1,0) 9 -> (1,2)
        
        q = collections.deque()
        q.append((1,0)) # (num, steps)
        visit = set()
        while q:
            num, steps = q.popleft()
            r, c = num_to_position(num)
            if board[r][c] != -1:
                num = board[r][c] # move to the destination of snake or ladder
            if num == N * N:
                return steps
            for i in range(1, 7):
                next_num = num + i
                if next_num <= N * N and next_num not in visit:
                    q.append((next_num, steps + 1))
                    visit.add(next_num)
        return -1
