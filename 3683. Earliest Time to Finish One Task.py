class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        l=[]
        for i in tasks:
            cal=sum(i)
            l.append(cal)
        return min(l)
