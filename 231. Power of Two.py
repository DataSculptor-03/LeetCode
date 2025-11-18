class Solution(object):
    def isPowerOfTwo(self, n):
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
                if n%2!=0:
                    count=0
                    break
                else:
                    n=n//2
        return count==1
