class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=nums
        s=set(nums)
        for i in s:
            if l.count(i)>len(l)/2:
                return i
