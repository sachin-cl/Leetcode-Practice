class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        tsum=0
        minlen=float('inf')
        l=0
        for r in range(len(nums)):
            tsum=tsum+nums[r]
            while tsum>=target:
                minlen=min(minlen,r-l+1)
                tsum=tsum-nums[l]
                l+=1
        if minlen==float('inf'):
            return 0
        else:
            return minlen    
        