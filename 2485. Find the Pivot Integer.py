class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=-1
        s1=0
        s2=0
        if n==1:
            return 1
        for i in range(n,-1,-1):
            s1+=i
            for j in range(i,-1,-1):
                s2+=j
            if s1==s2:
                count=i
                break
            s2=0
        return count
