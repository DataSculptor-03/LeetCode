class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        l = []
        for row in matrix:
            for num in row:  
                l.append(num)
        l.sort()
        return l[k-1]
