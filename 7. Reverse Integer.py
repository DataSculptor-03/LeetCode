class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        s = ''
        
        while x != 0:
            rem = x % 10
            s += str(rem)
            x //= 10

        if s == '':
            return 0 

        result = sign * int(s)
        
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
