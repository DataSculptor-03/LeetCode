class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=list(set(nums))
        l.sort()
        if len(l)>=3:
            return l[-3]
        else:
            return max(l)
