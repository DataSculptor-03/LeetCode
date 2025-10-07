class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a=0
        b=0
        for i in nums:
            if len(str(i))==1:
                a+=i
            else:
                b+=i
        if a==b:
            return False
        else:
            return True
