class Solution:
    def minInsertions(self, s: str) -> int:
        l=0
        ans=0
        for i in s:
            if i=="(":
                if l%2:
                    l-=1
                    ans+=1
                l+=2
            else:
                l-=1
                if l<0:
                    ans+=1
                    l=1
        return(l+ans)

        
                
        
                