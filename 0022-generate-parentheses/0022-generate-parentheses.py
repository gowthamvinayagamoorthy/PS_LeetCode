class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans=[]
        def pr(s,op,cl):
            if len(s)==n*2:
                ans.append(s)
                return 
            if op<n:
                pr(s+"(",op+1,cl)
            if cl<op:
                pr(s+")",op,cl+1)
        pr("",0,0)
        return ans