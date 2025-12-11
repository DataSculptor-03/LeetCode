class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = 0
        total_sum = sum(nums)
        result = []
        
        for i in range(n):
            left_sum = nums[i] * i - prefix_sum
            right_sum = (total_sum - prefix_sum - nums[i]) - nums[i] * (n - i - 1)
            result.append(left_sum + right_sum)
            prefix_sum += nums[i]
        
        return result
