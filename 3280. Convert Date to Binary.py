class Solution:
    def convertDateToBinary(self, date: str) -> str:
        s=date.split("-")
        st=""
        for i in s:
            n=int(i)
            bi=bin(n)[2:]
            st+=str(bi)+"-"
        return st[0:len(st)-1]
