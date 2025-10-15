class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        cal=(nums[-1]-1)*(nums[-2]-1)
        return cal
