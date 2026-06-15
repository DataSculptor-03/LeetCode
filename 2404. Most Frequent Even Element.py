class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        f = 0
        s = set(nums)

        for i in s:
            if i % 2 == 0 and nums.count(i) > f:
                f = nums.count(i)

        if f == 0:
            return -1

        l = []
        for i in s:
            if i % 2 == 0 and nums.count(i) == f:
                l.append(i)

        return min(l)
