class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        sf=float('inf')
        li=[]
        st=str(n)
        l=list(st)
        s=set(l)
        for i in s:
            if l.count(i)<sf:
                sf=l.count(i)
        for i in s:
            if l.count(i)==sf:
                li.append(i)
        li.sort()
        return int(li[0])
