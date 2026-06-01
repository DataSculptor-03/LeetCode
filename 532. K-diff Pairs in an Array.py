class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        s=set()
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    s.add(tuple(sorted((nums[i],nums[j]))))
        return len(s)
