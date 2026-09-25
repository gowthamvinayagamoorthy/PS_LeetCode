class Solution:
    def findCircleNum(self, l: List[List[int]]) -> int:
        g=[[]for _ in range(len(l))]
        for i in range(len(l)):
            for j in range(len(l[0])):
                if i==j:
                    continue
                if l[i][j]==1:
                    g[i].append(j)
        def dfs(s):
            if s in visi:
                return
            visi.add(s)
            for neib in g[s]:
                dfs(neib)
        visi=set()
        c=0
        for i in range(len(l)):
            if i not in visi:
                dfs(i)
                c+=1
        return c