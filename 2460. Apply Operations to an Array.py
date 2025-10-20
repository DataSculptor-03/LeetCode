class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1=[]
        l2=[]
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        for i in nums:
            if i==0:
                l1.append(i)
            else:
                l2.append(i)
        return l2+l1
        
