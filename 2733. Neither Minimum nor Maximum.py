class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)==2 or len(nums)==1:
            return -1
        elif len(nums)>2:
            return nums[1]
