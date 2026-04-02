class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count=0
        for i in range(0,len(startTime)):
            arr=[]
            for j in range(startTime[i],endTime[i]+1):
                arr.append(j)
            if queryTime in arr:
                count+=1
        return count
