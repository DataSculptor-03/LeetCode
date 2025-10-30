class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = nums1 + nums2
        n.sort()
        if len(n)%2!=0:
            return float(n[len(n)//2])
        else:
            v1=len(n)//2
            v2=(len(n)//2)-1
            cal=(n[v1]+n[v2])/2.0
            return cal
