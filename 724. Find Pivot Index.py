class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=0
        l1=[]
        l2=[]
        ans=-1
        for i in range(0,len(nums)):
            l1=nums[0:i]
            l2=nums[i+1:]
            if sum(l1)==sum(l2):
                ans=i
                break
        return ans
