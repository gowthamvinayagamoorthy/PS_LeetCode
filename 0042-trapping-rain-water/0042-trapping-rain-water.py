class Solution(object):
    def trap(self, height):
        lm=0
        rm=0
        water=0
        i=0
        j=len(height)-1
        while(i<j):
            lm=max(height[i],lm)
            rm=max(height[j],rm)
            if height[i]<height[j]:
                water+=lm-height[i]
                i+=1
            else:
                water+=rm-height[j]
                j-=1
        return water
        