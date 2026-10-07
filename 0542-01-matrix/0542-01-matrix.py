class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        from collections import deque
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        n=len(mat)
        m=len(mat[0])
        sol=[[0]*m for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    sol[i][j]=-1
                
    
        while q:
            r,c=q.popleft()
            for dr,dc in d:
                nr=r+dr
                nc=c+dc
                if 0<=nr<n and 0<=nc<m and sol[nr][nc]==-1:
                    sol[nr][nc]=sol[r][c]+1
                    q.append((nr,nc))
        return (sol)
                    