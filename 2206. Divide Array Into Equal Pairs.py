class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s=set(nums)
        div=len(nums)//2
        count=1
        for i in s:
            if nums.count(i)%2!=0:
                count=0
                break
        return count==1
