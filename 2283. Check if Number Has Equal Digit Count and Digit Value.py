class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        flag=1
        for i in range(len(num)):
            c=num.count(str(i))
            if c!=int(num[i]):
                flag=0
                break
        return flag==1
