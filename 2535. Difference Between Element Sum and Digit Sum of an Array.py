class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t=sum(nums)
        s=0
        for i in nums:
            if(len(str(i))==1):
                s+=int(i)
            else:
                while(i>=1):
                    rem=i%10
                    s+=rem
                    i//=10
        return abs(t-s)
