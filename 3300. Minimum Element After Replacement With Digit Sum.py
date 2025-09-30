class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in nums:
            s=0
            while(i>=1):
                rem=i%10
                s+=rem
                i//=10
            l.append(s)
        return min(l)
