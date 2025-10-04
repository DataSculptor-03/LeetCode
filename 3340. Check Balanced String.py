class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        os=0
        es=0
        for i in range(len(num)):
            if i%2==0:
                os+=int(num[i])
            else:
                es+=int(num[i])
        return es==os
