import math
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        m=math.prod(nums)
        if m>0:
            return 1
        elif m==0:
            return 0
        else:
            return -1
