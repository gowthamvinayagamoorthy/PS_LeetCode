from itertools import permutations
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        n=len(nums)
       
        for i in range(n):
            nums[i]=nums[i]**2
        nums.sort(reverse=True)
        
        ans=0
        i=0
        j=n-1
        pp=0
        while i<j:
            if pp==0:
                ans+=nums[i]
                pp=1
                i+=1
            if pp==1:
                ans-=nums[j]
                j-=1
                pp=0
            
        if n%2:
            ans+=nums[n//2]
        
        return (ans)