class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        from collections import deque
        print(image)
        row=len(image)
        col=len(image[0])
        q=deque()
        old=image[sr][sc]
        
        q=deque([(sr,sc)])
        image[sr][sc]=color
        v=[[sr,sc]]
        d=[(1,0),(0,1),(-1,0),(0,-1)]
        while q:
            print(q)
            r,c=q.popleft()
            for dr,dc in d:
                nr=r+dr
                nc=c+dc
                if 0<=nr<row and 0<=nc<col and image[nr][nc]==old:
                    if [nr,nc] not in v:
                        if image[nr][nc]==old:
                            image[nr][nc]=color
                        q.append([nr,nc])
                        v.append([nr,nc])
        return image
        
