class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        else:
            count=0
            for i in range(0,len(nums)-1):
                if nums[i]%2==0 and nums[i+1]%2!=0:
                    count=1
                elif nums[i]%2!=0 and nums[i+1]%2==0:
                    count=1
                else:
                    count=0
                    break
        return count==1
