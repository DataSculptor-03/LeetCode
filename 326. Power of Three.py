class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        count=1
        if n<=0:
            return False
        else:
            while(n!=1):
                if n%3!=0:
                    count=0
                    break
                else:
                    n=n//3
        return count==1
