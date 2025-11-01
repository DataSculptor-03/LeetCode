class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        li=[]
        for i in range(0,len(nums)-1):
            s=0
            for j in range(i+1,len(nums)):
                s=nums[i]+nums[j]
                if(s==target):
                    li.append(i)
                    li.append(j)
                    break;
                s=0
        return li
