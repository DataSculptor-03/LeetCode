class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        count=0
        for i in range(len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i]==2*arr[j] or arr[j]==2*arr[i]:
                    count=1
                    break
        return count==1
