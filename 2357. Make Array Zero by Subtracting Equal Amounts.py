class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        while(max(nums)!=0):
            mi=min([x for x in nums if x > 0])
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]=nums[i]-mi
            count+=1
        return count
