class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        left=0
        right=0
        for i in nums:
            if i>0:
                right+=i
                if left+right==0:
                    count+=1
            elif i<0:
                left+=i
                if left+right==0:
                    count+=1
        return count
