class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        t=0
        for i in range(len(s)-1):
            a1=ord(s[i])
            a2=ord(s[i+1])
            cal=abs(a1-a2)
            t+=cal
        return t
