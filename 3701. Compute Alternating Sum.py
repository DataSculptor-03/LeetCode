class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        e=[]
        o=[]
        for i in range(0,len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        return sum(e)-sum(o)
