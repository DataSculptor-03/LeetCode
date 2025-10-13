class Solution(object):
    def kthFactor(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        l=[]
        for i in range(1,n+1):
            if n%i==0:
                l.append(i)
        if k<=len(l):
            return l[k-1]
        else:
            return -1
