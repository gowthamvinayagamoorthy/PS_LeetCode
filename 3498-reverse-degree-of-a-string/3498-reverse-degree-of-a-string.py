class Solution:
    def reverseDegree(self, s: str) -> int:
        c=0
        for n,i in enumerate(s):
            num=26-(ord(i)-ord("a"))
            c+=num*(n+1)
        return c