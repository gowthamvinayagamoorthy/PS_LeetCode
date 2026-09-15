class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        from collections import deque
        visi={(0,0)}
        q=deque([(0,0)])
        while q:
            (a,b)=q.popleft()
            if a==target or b==target or a+b==target:
                return True
            st=[(a,0),(0,b),(a,y),(x,b),(a-min(a,y-b),b+min(a,y-b)),(a+min(b,x-a),b-min(b,x-a))]
            for ns in st:
                if ns not in visi:
                    visi.add(ns)
                    q.append(ns)
        return False
