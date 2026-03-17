class Solution:
    def removeZeros(self, n: int) -> int:
        st=str(n)
        s=""
        for i in st:
            if i!='0':
                s+=str(i)
        return int(s)
