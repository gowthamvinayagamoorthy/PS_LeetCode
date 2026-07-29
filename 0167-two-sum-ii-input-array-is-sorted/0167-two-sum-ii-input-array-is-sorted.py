class Solution:
    def twoSum(self, l: List[int], k: int) -> List[int]:
        i=0
        j=len(l)-1
        while i<j:
            if l[i]+l[j]==k:
                return [i+1,j+1]
            if l[i]+l[j]<k:
                i+=1
            else:
                j-=1