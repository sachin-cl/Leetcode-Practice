class Solution(object):
    def maxArea(self, height):
        l=0
        r=len(height)-1
        totalmax=0
        currmax=0
        while l<r:
            if height[l]>=height[r]:
                currmax=height[r]*(r-l)
                r=r-1
            elif height[l]<height[r]:
                currmax=height[l]*(r-l)
                l+=1
            totalmax=max(currmax,totalmax)
        return totalmax

