class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l=[]
        for i in range(1,n+1):
            if n%i==0:
                l.append(i)
        return len(l)==3
