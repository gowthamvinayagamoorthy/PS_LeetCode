class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st=[0]
        
        for i in s:
            if i =="(":
                st.append(0)
            else:
                iner=st.pop()
                if iner ==0:
                    sc=1
                else:
                    sc=2*iner
                st[-1]+=sc
        return st[0]