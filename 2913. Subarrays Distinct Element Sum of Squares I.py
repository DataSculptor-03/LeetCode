class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                l=nums[i:j+1]
                s=set(l)
                total+=(len(s))**2
        return total
