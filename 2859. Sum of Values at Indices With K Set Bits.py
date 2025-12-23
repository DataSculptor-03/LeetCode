class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s=0
        for i in range(0,len(nums)):
            bi=bin(i)[2:]
            if bi.count('1')==k:
                s+=nums[i]
        return s
