class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        l=[]
        for i in range(len(ranges)):
            st,en=ranges[i]
            for j in range(st,en+1):
                l.append(j)
        for i in range(left,right+1):
            if i not in l:
                return False
        return True
