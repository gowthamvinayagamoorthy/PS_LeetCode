class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        rem_right=0
        bal=0
        for i in s:
            if i=="(":
                bal+=1
            if i==")":
                if bal>0:
                    bal-=1
                else:
                    rem_right+=1
            
        rem_left=bal
        ans=set()
        def para(i,rem_left,rem_right,bal,curr):
            
            if i==len(s):
                if bal==0 and rem_left==0 and rem_right==0:
                    ans.add(curr)
                return
            ch=s[i]
            
            if ch=="(":
                if rem_left>0:
                    para(i+1,rem_left-1,rem_right,bal,curr)
                para(i+1,rem_left,rem_right,bal+1,curr+ch)
            elif ch==")":
                if rem_right>0:
                    para(i+1,rem_left,rem_right-1,bal,curr)
                if bal>0:
                    para(i+1,rem_left,rem_right,bal-1,curr+ch)
            else:
                para(i+1,rem_left,rem_right,bal,curr+ch)
        para(0,rem_left,rem_right,0,"")
        return list(ans)

