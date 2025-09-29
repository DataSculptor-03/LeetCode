class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[]
        count1=0
        count2=0
        for i in nums1:
            if i in nums2:
                count1+=1
        l.append(count1)
        for i in nums2:
            if i in nums1:
                count2+=1
        l.append(count2)
        return l
