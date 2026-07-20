class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d=defaultdict(int)
        i=0
        res=0
        for j in range(len(s)):
            d[s[j]]=d.get(s[j],0)+1
            maxfre=max(d.values())
            curlen=j-i+1
            if curlen-maxfre>k:
                d[s[i]]-=1
                i+=1
                curlen=j-i+1
            res=max(res,curlen)
        return res
        