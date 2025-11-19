class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s=''
        if num==0:
            return "0"
        is_negative = num < 0
        num = abs(num)
        while(num>0):
            rem=num%7
            s=str(rem)+s
            num//=7
        if is_negative:
            s = '-' + s

        return s
