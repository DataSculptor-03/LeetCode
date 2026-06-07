class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        l=[]
        for i in range(0,numOnes):
            l.append(1)
        for i in range(0,numZeros):
            l.append(0)
        for i in range(0,numNegOnes):
            l.append(-1)
        l.sort()
        l.reverse()
        arr=l[0:k]
        return sum(arr)
