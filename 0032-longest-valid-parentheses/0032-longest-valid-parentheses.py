class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st=[-1]
        mx=0
        for i,ch in enumerate(s):
            if ch=="(":
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    mx=max(mx,i-st[-1])
        return mx