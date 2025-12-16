class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        count=0
        for row in matrix:
            for i in row:
                if i==target:
                    count=1
                    break
        return count==1
