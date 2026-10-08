class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        bal=0
        res=""
        for i,ch in enumerate(s):
            if ch =="(":
                
                if bal>0:
                    res+=ch
                bal+=1
            else:
                bal-=1
                if bal>0:
                    res+=ch
                
            
        return (res)
        
            


        