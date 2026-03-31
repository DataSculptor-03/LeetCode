class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        m=0
        for i in range(0,len(nums)):
            if nums[i]==1:
                count+=1
                m=max(m,count)
            else:
                count=0
        return m
