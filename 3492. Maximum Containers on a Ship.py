class Solution(object):
    def maxContainers(self, n, w, maxWeight):
        """
        :type n: int
        :type w: int
        :type maxWeight: int
        :rtype: int
        """
        total = n * n
        for containers in range(total, -1, -1):
            if containers * w <= maxWeight:
                return containers
        return 0
