class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        if "0000" in deadends:
            return -1
        q=deque([("0000",0)])
        visi={"0000"}
        deads=set(deadends)
        while q:
            state,dist=q.popleft()
            if state==target:
                return dist
            for i in range(4):
                for incdec in [-1,1]:
                    newdig=(int(state[i])+incdec)%10
                    newstate=state[:i]+str(newdig)+state[i+1:]
                    if newstate not in deads and newstate not in visi:
                        q.append((newstate,dist+1))
                        visi.add(newstate)
        return -1