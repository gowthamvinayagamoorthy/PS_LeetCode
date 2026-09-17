class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans=[]
        def ipr(i,p):
            print(p)
            if len(p)==4:
                if i==len(s):
                    ans.append(".".join(p))
                return
            for j in range(1,4):
                if (j+i)>len(s):
                    break
                part=s[i:i+j]
                if len(part)>1 and part[0]=="0":
                    continue
                if int(part)>255:
                    continue
                p.append(part)
                ipr(i+j,p)
                p.pop()
            return
        ipr(0,[])
        return ans

            