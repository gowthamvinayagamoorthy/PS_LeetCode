class Solution:
    def shortestPathLength(self, g: List[List[int]]) -> int:
        n=len(g)
        fmask=(1<<n)-1
        visi=set()
        from collections import deque
        q=deque()
        for i in range(n):
            mask=1<<i
            q.append((i,mask,0))
        while q:
            node,mask,dist=q.popleft()
            if mask==fmask:
                return dist
            for neib in g[node]:
                nmask=mask|(1<<neib)
                state=(neib,nmask)
                if state not in visi:
                    visi.add(state)
                    q.append((neib,nmask,dist+1))
