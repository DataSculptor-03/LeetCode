import math
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        o=[]
        e=[]
        for i in range(1,(n*2)+1):
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        s1=sum(o)
        s2=sum(e)
        return math.gcd(s1,s2)
