class Solution:
    def maxFreqSum(self, s: str) -> int:
        ns=s.lower()
        l=list(ns)
        se=set(ns)
        vc=0
        cc=0
        for i in l:
            if i=='a' or i=='e' or i=='o' or i=='i' or i=='u':
                if l.count(i)>vc:
                    vc=l.count(i)
            else:
                if l.count(i)>cc:
                    cc=l.count(i)
        return vc+cc
