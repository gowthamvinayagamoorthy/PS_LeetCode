class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref=0
        c=0
        hm={0:1}
        for i in nums:
            pref+=i
            if pref%k in hm:
                c+=hm[pref%k]
            hm[pref%k]=hm.get(pref%k,0)+1
        return c
