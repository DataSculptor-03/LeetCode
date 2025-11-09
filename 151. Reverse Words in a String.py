class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1=''
        sp=s.split()
        for i in range(len(sp)-1,-1,-1):
            s1+=str(sp[i])
            s1+=" "
        return s1.strip()
