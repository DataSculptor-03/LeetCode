class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        l=[]
        while(len(nums)!=0):
            mi=min(nums)
            ma=max(nums)
            avg=(mi+ma)/2
            nums.remove(mi)
            nums.remove(ma)
            l.append(avg)
        s=set(l)
        return len(s)
