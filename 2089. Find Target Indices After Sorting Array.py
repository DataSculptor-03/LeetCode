class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        l=[]
        for i in range(0,len(nums)):
            if nums[i]==target:
                l.append(i)
        return l
