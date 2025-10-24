class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        c=s.count(letter)
        n=len(s)
        p=(c*100)/float(n)
        return int(p)
