class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        even_idx = 0
        odd_idx = 1
        
        for num in nums:
            if num % 2 == 0:
                l[even_idx] = num
                even_idx += 2
            else:
                l[odd_idx] = num
                odd_idx += 2
                
        return l
