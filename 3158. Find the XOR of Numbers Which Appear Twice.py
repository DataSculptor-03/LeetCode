class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        s=set(nums)
        cal=0
        for i in s:
            count=nums.count(i)
            if count>1:
                cal^=i
        return cal
