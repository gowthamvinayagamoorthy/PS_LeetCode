class Solution:
    def rob(self, l: List[int]) -> int:
        dp=[0]*len(l)
        for i in range(len(l)):
            if i<2:
                dp[i]=max(l[i],dp[i-1])
            else:
                dp[i]=max(dp[i-2]+l[i],dp[i-1])
    
        return dp[len(l)-1]
