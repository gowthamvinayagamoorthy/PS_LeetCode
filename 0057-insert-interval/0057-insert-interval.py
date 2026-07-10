class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        for l,r in intervals:
            if newInterval[0]>r:
                ans.append([l,r])
            elif newInterval[1]<l:
                ans.append([newInterval[0],newInterval[1]])
                newInterval=[l,r]
            else:
                newInterval[0]=min(newInterval[0],l)
                newInterval[1]=max(newInterval[1],r)
        ans.append(newInterval)
        return ans

