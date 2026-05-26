class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        m=max(num1,num2,num3)
        s=str(m)
        l=len(s)
        s1=str(num1).zfill(l)
        s2=str(num2).zfill(l)
        s3=str(num3).zfill(l)
        s1.split()
        s2.split()
        s3.split()
        s4=""
        for i in range(0,len(s1)):
            mi=min(int(s1[i]),int(s2[i]),int(s3[i]))
            s4+=str(mi)
        return int(s4)
