class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        s=set(nums)
        l=list(s)
        l.sort()
        l.reverse()
        return l[0:k]
