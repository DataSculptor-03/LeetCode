class Solution:
    def reverseBits(self, n: int) -> int:
        bi=format(n,'032b')
        rev=bi[::-1]
        return int(rev,2)
