class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num=n
        t=0
        m=1
        while(n!=0):
            rem=n%10
            t+=rem
            m*=rem
            n//=10
        to=t+m
        if num%to==0:
            return True
        else:
            return False
