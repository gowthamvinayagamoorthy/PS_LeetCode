class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        p={")":"(","}":"{","]":"["}
        for i in s:
            if i in "({[":
                st.append(i)
            else:
                if not(st) or st[-1]!=p[i]:
                    return False
                st.pop()
        return not(st)