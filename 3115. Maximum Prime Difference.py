class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        def prime(n):
            if n<2:
                return 0
            for i in range(2,(n//2)+1):
                if n%i==0:
                    return 0
            return 1

        for i in range(len(nums)):
            if prime(nums[i]):
                l.append(i)
        if len(l)==0:
            return 0
        elif len(l)==1:
            return 0
        else:
            return max(l)-min(l)
