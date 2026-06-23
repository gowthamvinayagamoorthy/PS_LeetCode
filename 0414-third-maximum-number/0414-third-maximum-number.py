class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        m1=m2=m3=float('-inf')
        for i in nums:
            if i==m1 or i==m2 or i==m3:
                continue 
            if i>m1:
                m3=m2
                m2=m1
                m1=i
            elif i>m2:
                m3=m2
                m2=i
            elif i>m3:
                m3=i
        return m3 if m3!= float('-inf') else m1