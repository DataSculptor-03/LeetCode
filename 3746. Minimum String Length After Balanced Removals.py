class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        s.split()
        se=set(s)
        count1=0
        count2=0
        for i in se:
            if i=='a':
                count1=s.count(i)
            else:
                count2=s.count('b')
        return abs(count1-count2)
