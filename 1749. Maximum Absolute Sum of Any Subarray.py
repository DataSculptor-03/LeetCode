class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_ending = max_sum = 0
        min_ending = min_sum = 0

        for x in nums:
            max_ending = max(x, max_ending + x)
            max_sum = max(max_sum, max_ending)

            min_ending = min(x, min_ending + x)
            min_sum = min(min_sum, min_ending)

        return max(max_sum, abs(min_sum))
