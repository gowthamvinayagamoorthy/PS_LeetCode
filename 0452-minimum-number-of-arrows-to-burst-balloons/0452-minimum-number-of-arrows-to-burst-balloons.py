class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        i=0
        j=1
        ar=1
        while i<len(points) and j<len(points):
            if points[i][1]<points[j][0]:
                i=j
                j+=1
                ar+=1
            else:
                j+=1
        return ar