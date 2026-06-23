class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def restr(n):
            k=10
            s=0
            for i in range(len(n)):
                s+=int(n[i])*(10**(len(n)-i-1))
            return s
        if num1=="0" and num2=="0":
            return "0"
        val=""
        res=restr(num1)+restr(num2)
        while(res>0):
            val+=str(res%10)
            res=res//10
        return val[::-1]


        
