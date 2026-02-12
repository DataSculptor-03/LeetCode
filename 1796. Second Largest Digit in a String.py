class Solution:
    def secondHighest(self, s: str) -> int:
        di=[]
        for i in range(0,len(s)):
            if s[i].isnumeric():
                di.append(int(s[i]))
        s=set(di)
        l=list(s)
        if len(l)==1 or len(l)==0:
            return -1
        else:
            l.sort()
            return l[len(l)-2]
