class Solution:
    def smallestNumber(self, n: int) -> int:
        bi=bin(n)[2:]
        s=bi.replace('0','1')
        return int(s,2)
