class Solution:
    def rotate(self, m: List[List[int]]) -> None:
        n=len(m)
        for i in range(n):
            for j in range(n):
                if i<j:
                    m[i][j],m[j][i]=m[j][i],m[i][j]
        for i in range(n):
            k=0
            j=n-1
            while k<j:
                m[i][k],m[i][j]=m[i][j],m[i][k]
                k+=1
                j-=1
        return m
            
            
        