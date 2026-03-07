class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = [0] * (n + 1)
        duplicate = missing = -1
        for num in nums:
            freq[num] += 1
        for i in range(1, n + 1):
            if freq[i] == 0:
                missing = i
            elif freq[i] == 2:
                duplicate = i
        return [duplicate, missing]
