class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count=1
        se=set(s)
        oc=s.count(s[0])
        for i in set(s):
            if oc!=s.count(i):
                count=0
                break
        return count==1
