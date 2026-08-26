class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        m=0
        def dfs(x,y):
            if x<0 or y<0 or x>row-1 or y>col-1 or grid[x][y]=="0":
                return
            grid[x][y]="0"
            dfs(x,y+1)
            dfs(x+1,y)
            dfs(x,y-1)
            dfs(x-1,y)
            return
        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    dfs(i,j)
                    m+=1
        return m
            