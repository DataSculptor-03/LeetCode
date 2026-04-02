class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        l=[]
        for i in range(0,len(nums)-1):
            l.append(abs(nums[i]-nums[i+1]))
        l.append(abs(nums[-1]-nums[0]))
        return max(l)
