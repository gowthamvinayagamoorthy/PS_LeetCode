class Solution:
    def candy(self, rat: list[int]) -> int:
        cand=[1]*len(rat)
        for i in range(1,len(rat)):
            if rat[i]>rat[i-1]:
                cand[i]=cand[i-1]+1
        
        for i in range(len(rat)-2,-1,-1):
            if rat[i]>rat[i+1]:
                cand[i]=max(cand[i],cand[i+1]+1)
        
        return sum(cand)