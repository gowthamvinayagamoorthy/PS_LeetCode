class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n=len(nums)
        res=0

        for i in range(n):
            h=set()
            for j in range(i,n):
                h.add(nums[j])
                res+=len(h)**2
        return res

                
                