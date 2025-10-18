class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        l=[]
        for i in s:
            l.append(nums.count(i))
        maxf=max(l)
        for i in l:
            c=l.count(maxf)
            return c*maxf
        
