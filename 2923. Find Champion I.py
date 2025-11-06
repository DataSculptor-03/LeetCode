class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=0
        index=-1
        for i in range(len(grid)):
            cal=grid[i].count(1)
            if cal>m:
                m=cal
                index=i
        return index
