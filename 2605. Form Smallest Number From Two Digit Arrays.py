class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)

        if common:
            return min(common)

        m1 = min(nums1)
        m2 = min(nums2)

        return int(str(min(m1, m2)) + str(max(m1, m2)))
