class Solution:
    def toHex(self, num: int) -> str:
        if num>0:
            cal=hex(num)[2:]
            return str(cal)
        elif num<0:
            cal=hex(num & 0xFFFFFFFF)
            return str(cal)[2:]
        elif num==0:
            return "0"
