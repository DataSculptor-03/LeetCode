class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums1:
            idx = nums2.index(num)  
            next_greater = -1
            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    next_greater = nums2[j]
                    break
            res.append(next_greater)
        return res
