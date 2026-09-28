class Solution:
    def jump(self, nums: list[int]) -> int:
        farth=0
        reach=0
        jump=0
        for i in range(len(nums)-1):
            farth=max(farth,i+nums[i])
            if i==reach:
                jump+=1
                reach=farth
        return jump
