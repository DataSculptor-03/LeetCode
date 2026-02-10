class Solution:
    def maxScore(self, s: str) -> int:
        l=[]
        for i in range(0,len(s)-1):
            s1=s[0:i+1]
            s2=s[i+1:len(s)]
            t=0
            t+=s1.count('0')
            t+=s2.count('1')
            l.append(t)
        return max(l)
