class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        p=0
        
        while r<len(prices):
            if prices[l]>prices[r]:
                l=r
                r+=1
            else:
                if p<(prices[r]-prices[l]):
                    p=prices[r]-prices[l]
                r+=1
        return p