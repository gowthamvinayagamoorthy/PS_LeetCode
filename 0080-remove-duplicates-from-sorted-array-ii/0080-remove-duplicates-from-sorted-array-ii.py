class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        J=2
        for i in range(2,len(nums)):
            if nums[i]!= nums[J-2]:
                nums[J]=nums[i]
                J+=1
        return J

