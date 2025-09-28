class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l1=nums[2:]
        l1.reverse()
        l2=nums[0:2]
        l2.reverse()
        return l2+l1
