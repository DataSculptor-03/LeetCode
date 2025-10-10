class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count=0
        nh = sorted(heights)
        for i in range(len(heights)):
            if heights[i]!=nh[i]:
                count+=1
        return count
