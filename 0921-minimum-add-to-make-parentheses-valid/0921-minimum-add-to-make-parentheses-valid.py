class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        k=0
        ans=0
        for i in s:
            if i=="(":
                k+=1
            else:
                if k>0:
                    k-=1
                else:
                    ans+=1
            
        return (ans+k)