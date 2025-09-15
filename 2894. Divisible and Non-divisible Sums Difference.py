class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        l1=[]
        l2=[]
        for i in range(1,n+1):
            if i%m==0:
                l2.append(i)
            else:
                l1.append(i)
        d=sum(l1)-sum(l2)
        return d
