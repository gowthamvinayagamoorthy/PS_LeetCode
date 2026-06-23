class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k%=len(nums)
        if k==0:
            return
        m=len(nums)-k
        l=[]
        if len(nums)==1:
            return
        for i in range(len(nums)):
            l.append(nums[m])
            m+=1
            if m==len(nums):
                m=0
        nums[:]=l
                
        