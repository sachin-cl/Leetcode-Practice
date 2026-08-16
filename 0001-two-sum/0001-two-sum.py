class Solution(object):
    def twoSum(self, nums, target):
        d={}
        for i ,j in enumerate(nums):
            d[j]=i
        for i,j in enumerate(nums):
            diff=target-j
            if diff in d and d[diff]!=i:
                return [i,d.get(diff)]
            