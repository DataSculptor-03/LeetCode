class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD=10**9 + 7
        l=[]
        for i in range(0,len(nums)):
            cal=0
            for j in range(i,len(nums)):
                cal+=nums[j]
                l.append(cal)
        l.sort()
        arr=l[left-1:right]
        return sum(arr)%MOD
