class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        n=x
        s=0
        while(x!=0):
            rem=x%10
            s+=rem
            x//=10
        if n%s==0:
            return s
        else:
            return -1
