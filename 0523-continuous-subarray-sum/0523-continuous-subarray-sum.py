class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref=0
        hm={0:-1}
        for i in range(len(nums)):
            pref+=nums[i]
            m=pref%k
            if m in hm:
                if i-hm[m]>=2:
                    return True
            else:
                hm[m]=i
        return False