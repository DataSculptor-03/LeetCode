class Solution(object):
    def checkPrimeFrequency(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def prime(n):
            if n<2:
                return False
            for i in range(2,n//2+1):
                if n%i==0:
                    return False
            return True

        s=set(nums)
        for i in s:
            c=nums.count(i)
            if prime(c):
                return True
        return False
