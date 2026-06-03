class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        s.split()
        l=[]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                cal=int(s[i])*int(s[j])
                l.append(cal)
        return max(l)
