class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        t=''
        for i in words:
            t+=i[0]
        return t==s
