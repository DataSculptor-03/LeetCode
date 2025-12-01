class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        if len(nums)==1:
            return 0
        else:
            nums.sort()
            for i in range(0,len(nums)-1):
                cal=nums[i+1]-nums[i]
                l.append(cal)
                cal=0
            return max(l)
