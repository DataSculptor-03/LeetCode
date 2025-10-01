class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        s = 0
        while n > 0:
            rem = n % 10
            m *= rem
            s += rem
            n //= 10
        return m - s
