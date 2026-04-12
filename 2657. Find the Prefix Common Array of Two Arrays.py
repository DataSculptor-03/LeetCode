class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        l=[]
        for i in range(1,len(A)+1):
            count=0
            a=A[0:i]
            b=B[0:i]
            for j in a:
                if j in b:
                    count+=1
            l.append(count)
        return l
