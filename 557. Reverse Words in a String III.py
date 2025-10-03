class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=''
        sp=s.split()
        for i in sp:
            n+=i[::-1]
            n+=' '
        return n[0:len(n)-1]
