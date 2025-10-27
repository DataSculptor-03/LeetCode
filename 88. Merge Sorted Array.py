class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        arr1=nums1[0:m]
        arr1.sort()
        arr2=nums2[0:n]
        arr2.sort()
        ne=arr1+arr2
        ne.sort()
        for i in range(m+n):
            nums1[i]=ne[i]
        return nums1
