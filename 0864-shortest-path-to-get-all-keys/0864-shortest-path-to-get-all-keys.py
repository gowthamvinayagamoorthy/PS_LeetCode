class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        from collections import deque
        n=len(grid)
        m=len(grid[0])
        keys=0
        kc=0
        key_set="abcdef"
        lock_set="ABCDEF"
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        sx,sy=0,0
        for i in range(n):
            for j in range(m):
                if grid[i][j] in key_set:
                    kc+=1
                if grid[i][j]=="@":
                    sx,sy=i,j
        q=deque([(sx,sy,keys,0)])
        visi={(sx,sy,keys)}
        while q:
            r,c,key,dist=q.popleft()
            if key==(1<<kc)-1:
                return dist
            for dr,dc in d:
                nr=dr+r
                nc=dc+c
                if 0<=nr<n and 0<=nc<m:
                    if grid[nr][nc]!="#":
                        nkeys=key
                        if grid[nr][nc] in key_set:
                            nkeys=key|(1<<(ord(grid[nr][nc])-ord("a")))

                        if grid[nr][nc] in lock_set:
                            if not(nkeys & (1<<(ord(grid[nr][nc])-ord("A")))):
                                continue

                        state=((nr,nc,nkeys))
                        if state not in visi:
                            visi.add((nr,nc,nkeys))
                            q.append((nr,nc,nkeys,dist+1))
                        
        return -1
                


                            
