class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for n in nums:
            idx = abs(n) - 1
            if nums[idx] < 0:
                res.append(abs(n))
            else:
                nums[idx] *= -1
        return res
