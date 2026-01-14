class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        count1=1
        count2=1
        for i in range(0,len(nums)-1):
            if nums[i] < nums[i + 1]:
                count1 = 0
            elif nums[i] > nums[i + 1]:
                count2 = 0

        return count1 == 1 or count2 == 1
