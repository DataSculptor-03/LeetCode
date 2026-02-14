class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(0,len(nums)):
            arr1=nums[0:i+1]
            arr2=nums[i+1:len(nums)]
            s1=set(arr1)
            s2=set(arr2)
            l.append(len(s1)-len(s2))
        return l
