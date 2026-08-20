class Solution:
    def getMaximumGold(self, g: List[List[int]]) -> int:
        def find(x,y,gg):
            if x>=len(g) or y>=len(g[0]) or x<0 or y<0 or v[x][y]==1 or g[x][y]==0:
                return
        
            v[x][y]=1
            
            gg+=g[x][y]
            ans[0]=max(gg,ans[0])
            find(x+1,y,gg)
            find(x,y+1,gg)
            find(x-1,y,gg)
            find(x,y-1,gg)
            v[x][y]=0
            return
        ans=[0]
       
        for i in range(len(g)):
            for j in range(len(g[0])):
                if g[i][j]!=0:
                    v=[[0]*len(g[0]) for _ in range(len(g))]
                    find(i,j,0)
                    
        return ans[0]