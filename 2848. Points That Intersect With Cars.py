class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        l=[]
        for i in nums:
            for j in range(i[0],i[1]+1):
                if j not in l:
                    l.append(j)
        return len(l)
