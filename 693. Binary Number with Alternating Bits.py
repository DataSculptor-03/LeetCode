class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bi=bin(n)[2:]
        s=str(bi)
        count=1
        for i in range(0,len(s)-1):
            if s[i]==s[i+1]:
                count=0
                break
        return count==1
