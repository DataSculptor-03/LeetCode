class Solution:
    def findComplement(self, num: int) -> int:
        bi=bin(num)[2:]
        s=str(bi)
        s1=""
        for i in s:
            if i=='0':
                s1+=str('1')
            else:
                s1+=str('0')
        return int(s1,2)
