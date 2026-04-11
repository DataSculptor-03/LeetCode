class Solution:
    def alternateDigitSum(self, n: int) -> int:
        t=0
        s=str(n)
        s.split()
        for i in range(len(s)):
            if i%2==0:
                t+=int(s[i])
            else:
                t-=int(s[i])
        return t
