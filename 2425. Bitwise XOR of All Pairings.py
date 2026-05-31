class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        xor2 = 0
        
        for x in nums1:
            xor1 ^= x
        
        for y in nums2:
            xor2 ^= y
        
        ans = 0
        if len(nums2) % 2 == 1:
            ans ^= xor1
        if len(nums1) % 2 == 1:
            ans ^= xor2
            
        return ans
