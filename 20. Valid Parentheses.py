class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=''
        while '()' in s or '{}' in s or '[]' in s:
            s=s.replace('()','')
            s=s.replace('{}','')
            s=s.replace('[]','')
        return len(s)==0
