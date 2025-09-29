class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]==nums[j]):
                    mul=i*j
                    if(mul%k==0):
                        count+=1
                mul=1
        return count
