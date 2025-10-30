class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s=''
        t=0
        while(n!=0):
            rem=n%2
            s+=str(rem)
            n//=2
        for i in s:
            t+=int(i)
        return t
