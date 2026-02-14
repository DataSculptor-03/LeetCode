class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        arr=nums1+nums2+nums3
        s=set(arr)
        l=[]
        for i in s:
            if (i in nums1 and i in nums2) or (i in nums2 and i in nums3) or (i in nums1 and i in nums3):
                l.append(i)
        return l
