class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        row=len(grid)
        col=len(grid[0])
        q=deque()
        f=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    f+=1
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        m=0
        while q and f:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in d:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                        grid[nr][nc]=2
                        f-=1
                        q.append((nr,nc))
            m+=1
        return m if f==0 else -1
    

