class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m=max(arr)
        for i in range(len(arr)):
            if arr[i]==m:
                return i
