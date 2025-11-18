class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count=1
        if n<=0:
            return False
        elif n==1:
            return True
        else:
            while(n!=1):
                if n%4!=0:
                    count=0
                    break
                else:
                    n=n//4
        return count==1
