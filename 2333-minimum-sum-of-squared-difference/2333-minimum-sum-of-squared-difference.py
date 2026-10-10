class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k=k1+k2
        
        gappy=[abs(nums1[i]-nums2[i]) for i in range(len(nums1))]
        if k>=sum(gappy):
            return 0
        maxi=max(gappy)

        c_arr=[0]* (maxi+1)
        for i in gappy:
            c_arr[i]+=1

        for i in range(maxi,0,-1):
            evlo_kuraika_mudiyu=min(k,c_arr[i])
            c_arr[i]-=evlo_kuraika_mudiyu
            
            c_arr[i-1]+=evlo_kuraika_mudiyu
            k-=evlo_kuraika_mudiyu

            if k==0:
                break
        ans=0
        for i in range(1,maxi+1):
            if c_arr[i]>0:

                ans+=(c_arr[i]*(i**2))
        return ans