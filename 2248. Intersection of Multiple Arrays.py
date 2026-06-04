class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l=[]
        for i in range(0,len(nums[0])):
            for j in range(1,len(nums)):
                if nums[0][i] not in nums[j]:
                    break
            else:
                l.append(nums[0][i])
        l.sort()
        return l
