class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr=[]
        for i in range(0,n):
            arr.append(start+2*i)
        val=0
        for i in arr:
            val^=i
        return val
