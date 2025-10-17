class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        for i in nums:
            digits=[]
            while(i>0):
                digits.append(i%10)
                i//=10
            l.extend(reversed(digits))
        return l
