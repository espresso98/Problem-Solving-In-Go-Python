# O(M*N), O(M*N)
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:     
        R, C = len(image), len(image[0])
        cur_color = image[sr][sc]

        if cur_color == color: 
            return image       # no changes

        def dfs(r, c):
            if (0 <= r < R and 0 <= c < C) and image[r][c] == cur_color:
                image[r][c] = color
                for i, j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    dfs(r+i, c+j) 

        dfs(sr, sc)
        return image
        