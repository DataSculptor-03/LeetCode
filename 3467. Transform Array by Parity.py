class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=0
        nr=1
        l=[]
        for i in nums:
            if i%2==0:
                l.append(r)
            else:
                l.append(nr)
        l.sort()
        return l
