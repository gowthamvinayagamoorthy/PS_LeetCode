class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        p=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                p+=prices[i]-prices[i-1]
        return p