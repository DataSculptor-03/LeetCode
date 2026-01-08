class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        n = len(nums)
        return [i for i in range(1, n + 1) if i not in s]
