class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count=0
        def prime(n):
            if n<2:
                return 0
            for i in range(2,(n//2)+1):
                if n%i==0:
                    return 0
            return 1
        for i in range(left,right+1):
            bi=bin(i)[2:]
            s=str(bi)
            c=s.count('1')
            if prime(c):
                count+=1
        return count
