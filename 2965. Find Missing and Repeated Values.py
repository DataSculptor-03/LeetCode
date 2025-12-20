class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l = []
        nums = [x for row in grid for x in row]
        n=len(grid)

        for i in range(1, n*n + 1):
            if nums.count(i) > 1:
                l.append(i)

        for i in range(1, n*n + 1):
            if i not in nums:
                l.append(i)

        return l
