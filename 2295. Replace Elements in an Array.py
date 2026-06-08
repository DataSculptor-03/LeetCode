class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        pos = {v: i for i, v in enumerate(nums)}
        for old, new in operations:
            idx = pos[old]
            nums[idx] = new    
            pos[new] = idx     
            del pos[old]       
        return nums
