class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                cal=nums[i-1]-nums[i]+1
                nums[i]=nums[i]+cal
                count+=cal
            if nums[i]==nums[i-1]:
                nums[i]=nums[i]+1
                count+=1
        return count
