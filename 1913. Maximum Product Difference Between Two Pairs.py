class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        f=nums[-1]*nums[-2]
        s=nums[0]*nums[1]
        return f-s
