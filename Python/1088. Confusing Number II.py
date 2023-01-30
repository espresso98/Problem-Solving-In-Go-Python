class Solution1:
    def confusingNumberII(self, n: int) -> int:
        rotation = {0:0, 1:1, 6:9, 8:8, 9:6}
        self.res = 0

        def dfs(num, numRotated, base):
            if num != numRotated:
                self.res += 1
            for d, dRotated in rotation.items():
                if d == 0 and num == 0: continue  
                if num * 10 + d > n: break  
                dfs(num * 10 + d, dRotated * base + numRotated, base * 10)
                # (1 1 10) (10 1 100) (11 11 100) (16 91 100) (18 81 100) (19 61 100) (6 9 10) (8 8 10) (9 6 10)
        dfs(0, 0, 1)
        return self.res


class Solution2:
    def confusingNumberII(self, n: int) -> int:
        def dfs(cur: int, rotation: int, base: int) -> int:
            res = 0 
# (0,0,1) (1 1 10) (10 1 100) (11 11 100) (16 91 100) (18 81 100) (19 61 100) (6 9 10) (8 8 10) (9 6 10)
            if cur != rotation:  
                res += 1       # 10, 1 / 16, 91 / 18, 81 / 19, 61 / 6, 9 / 9, 6 
            for digit in mapping:        
                next = cur * 10 + digit  # 0 1 10 100 101 106 108 109 11 
                if 0 < next <= n:
                    res += dfs(next, mapping[digit] * base + rotation, base * 10)
            return res

        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        return dfs(0,0,1)
        