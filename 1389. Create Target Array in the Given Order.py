class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        l=[]
        j=0
        for i in nums:
            l.insert(index[j],i)
            j+=1
        return l
