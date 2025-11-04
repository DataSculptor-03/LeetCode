class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def fact(n):
            if n==0:
                return 1
            else:
                result=1
                for i in range(1,n+1):
                    result*=i
                return result
        facto=fact(n)
        s=str(facto)
        s1=s.rstrip('0')
        return len(s)-len(s1)
