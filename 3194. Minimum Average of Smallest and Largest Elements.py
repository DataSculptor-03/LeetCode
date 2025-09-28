class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        n=len(nums)//2
        l=[]
        for i in range(0,n):
            mi=min(nums)
            ma=max(nums)
            avg=(mi+ma)/2.0
            l.append(avg)
            nums.remove(mi)
            nums.remove(ma)
        return min(l)
