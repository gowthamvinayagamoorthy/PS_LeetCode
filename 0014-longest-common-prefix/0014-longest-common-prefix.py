class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        print(strs)
        f=strs[0]
        l=strs[-1]
        res=""
        for i in range(min(len(f),len(l))):
            if f[i]!=l[i]:
                break
            res+=f[i]
        return res