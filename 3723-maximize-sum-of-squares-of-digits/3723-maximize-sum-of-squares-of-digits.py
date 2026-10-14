class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ""
        while len(res) < num:
            mini = min(9, sum)
            
            res += str(mini)
            sum-=mini
        if sum>0:
            return ""
        return (res)
