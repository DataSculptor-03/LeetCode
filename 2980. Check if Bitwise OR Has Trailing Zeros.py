class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                cal = nums[i] | nums[j]  
                if cal % 2 == 0:
                    return True
        return False
