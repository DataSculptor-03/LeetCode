class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        l=[]
        for i in nums:
            l.append(i*i)
        l.sort()
        return l
