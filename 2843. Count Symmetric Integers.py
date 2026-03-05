class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low,high+1):
            if len(str(i))%2==0:
                l=len(str(i))
                di=l//2
                arr1=str(i)[0:di]
                arr2=str(i)[di:l]
                l1=list(arr1)
                li1=list(map(int,l1))
                l2=list(arr2)
                li2=list(map(int,l2))
                if sum(li1)==sum(li2):
                    count+=1
        return count
