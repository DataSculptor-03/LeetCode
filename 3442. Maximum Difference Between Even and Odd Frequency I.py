class Solution(object):
    def maxDifference(self, s):
        """
        :type s: str
        :rtype: int
        """
        o=[]
        e=[]
        se=set(s)
        for i in se:
            count=s.count(i)
            if count%2==0:
                e.append(count)
            else:
                o.append(count)
        return max(o)-min(e)
