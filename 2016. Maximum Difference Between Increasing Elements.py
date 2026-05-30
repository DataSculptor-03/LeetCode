class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        d=-1
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if (0<=i<j<len(nums)) and (nums[i]<nums[j]):
                    if nums[j]-nums[i]>d:
                        d=nums[j]-nums[i]
        return d
