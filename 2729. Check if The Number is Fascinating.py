class Solution:
    def isFascinating(self, n: int) -> bool:
        s=""
        for i in range(1,4):
            num=n*i
            s+=str(num)
        count=1
        l=list(s)
        for i in range(1,10):
            if str(i) not in l or l.count(str(i))>1:
                count=0
                break
        return count==1
