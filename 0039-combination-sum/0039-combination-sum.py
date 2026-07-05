class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        p=[]
        def findt(i,s):
            if i>=len(candidates) or s>target:
                return
            if s==target:
                res.append(p.copy())
                return
            p.append(candidates[i])
            findt(i,s+candidates[i])
            p.pop()
            findt(i+1,s)
            return
        findt(0,0)
        return res