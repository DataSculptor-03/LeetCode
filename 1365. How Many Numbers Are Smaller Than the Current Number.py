class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in range(0,len(nums)):
            count=0
            for j in range(0,len(nums)):
                if nums[i]>nums[j]:
                    count+=1
            l.append(count)
        return l
