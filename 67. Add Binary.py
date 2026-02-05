class Solution:
    def addBinary(self, a: str, b: str) -> str:
        t=bin(int(a,2)+int(b,2))
        return str(t)[2:]
