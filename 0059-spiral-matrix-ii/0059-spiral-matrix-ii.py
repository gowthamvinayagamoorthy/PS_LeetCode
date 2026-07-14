class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ma=[[0]*n for _ in range(n)]
        t,l=0,0
        b,r=n-1,n-1
        k=1
        while t<=b and l<=r:
            for i in range(l,r+1):
                ma[t][i]=k
                k+=1
            t+=1
            for i in range(t,b+1):
                ma[i][r]=k
                k+=1
            r-=1
            if l<=b:
                for i in range(r,l-1,-1):
                    ma[b][i]=k
                    k+=1
            b-=1
            if l<=r:
                for i in range(b,t-1,-1):
                    ma[i][l]=k
                    k+=1
            l+=1
        for o in ma:
            print(o)
        return ma


