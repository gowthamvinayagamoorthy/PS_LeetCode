class Solution(object):
    def uniquePathsIII(self, grid):
        n=len(grid)
        m=len(grid[0])
        sol=[[0]*m for _ in range(n)]
        p=[0]
        
        def findp(x,y,c):
    
            if x>=n or y>=m or x<0 or y<0 or grid[x][y]==-1 or sol[x][y]==1:
                return
            if grid[x][y]==2:
                if c==tot_steps:
                    p[0]+=1
                return
            sol[x][y]=1
            findp(x+1,y,c+1)
            findp(x,y+1,c+1)
            findp(x-1,y,c+1)
            findp(x,y-1,c+1)
            sol[x][y]=0
            return
        k=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    sx=i
                    sy=j
                if grid[i][j]==-1:
                    k+=1
        tot_steps=n*m-k
        findp(sx,sy,1)
        return p[0]




        