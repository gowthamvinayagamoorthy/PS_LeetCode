class Solution:
    def coinChange(self, coins: List[int], amt: int) -> int:
        dp=[[float('inf')]*(amt+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=0
            for j in range(1,amt+1):
                if j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i]])
        
        if dp[len(coins)-1][amt]==float('inf'):
            return -1
        else:
            return dp[len(coins)-1][amt]