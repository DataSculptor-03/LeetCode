class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        s=set(nums)
        for i in s:
            if nums.count(i)==2:
                l.append(i)
        return l
