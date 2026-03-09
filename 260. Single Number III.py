class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s=set(nums)
        l=[]
        for i in s:
            if nums.count(i)==1:
                l.append(i)
        return l
