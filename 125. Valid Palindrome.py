class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1=''
        for i in s:
            if i.isalnum():
                s1+=i
        s1=s1.lower()
        return s1[0:]==s1[::-1]
