class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        first=0
        for i in range(0,len(nums)-1):
            first+=nums[i]
            rest=0
            for j in range(i+1,len(nums)):
                rest+=nums[j]
            if (first+rest)%2==0:
                count+=1
        return count
