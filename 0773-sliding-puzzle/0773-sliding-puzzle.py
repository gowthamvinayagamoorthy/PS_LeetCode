class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        from collections import deque

        def generatestate(m):
            g = []
            for u in range(len(m)):
                for v in range(len(m[0])):
                    if m[u][v] == 0:
                        i=u
                        j=v
            if -1 < i - 1 < len(m) and -1 < j < len(m[0]):
                s1=[ r.copy() for r in m]
                s1[i - 1][j], s1[i][j] = s1[i][j], s1[i - 1][j]
                g.append(s1)
            if -1 < i < len(m) and -1 < j - 1 < len(m[0]):
                s2 = [r.copy() for r in m]
                s2[i][j - 1], s2[i][j] = s2[i][j], s2[i][j - 1]
                g.append(s2)
            if -1 < i + 1 < len(m) and -1 < j < len(m[0]):
                s3 = [r.copy() for r in m]
                s3[i + 1][j], s3[i][j] = s3[i][j], s3[i + 1][j]
                g.append(s3)
            if -1 < i < len(m) and -1 < j + 1 < len(m[0]):
                s4 = [r.copy() for r in m]
                s4[i][j + 1], s4[i][j] = s4[i][j], s4[i][j + 1]
                g.append(s4)
            return g
        q=deque([(board,0)])
        visi=[board]
        tar=[[1,2,3],[4,5,0]]
        
        while q:
            st,dist=q.popleft()
            if st==tar:
                return dist
            print(st)
            for k in generatestate(st):
                if k not in visi:
                    q.append((k,dist+1))
                    visi.append(k)
        return -1

        