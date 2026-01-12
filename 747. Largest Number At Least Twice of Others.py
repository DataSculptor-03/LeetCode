class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        count=-1
        s=set(nums)
        l=list(s)
        l.sort()
        if l[-1]>=2*l[-2]:
            count=nums.index(l[-1])
        return count
