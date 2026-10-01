class Solution:
    def canCompleteCircuit(self, g: list[int], c: list[int]) -> int:
        t=0
        b=0
        st=0
        for i in range(len(g)):
            t+=g[i]-c[i]
            b+=g[i]-c[i]
            if b<0:
                st=i+1
                b=0
        if t<0:
            return -1
        return st