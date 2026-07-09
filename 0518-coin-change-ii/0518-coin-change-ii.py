class Solution:
    def change(self, amt: int, coins: List[int]) -> int:
        dp=[[0] * (1+amt) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=1
            for j in range(amt+1):
                if i==0 and j%coins[i]==0 :
                    dp[0][j]=1
                elif j<coins[i]:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-coins[i]]
        return dp[len(coins)-1][amt]