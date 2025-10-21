class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=-1
        nums.sort()
        for i in nums:
            if -i in nums:
                count=-i
                break
        return count
