class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        extra = []
        for i in nums:
            s = str(i)
            t = s[::-1]
            extra.append(int(t))
        nums.extend(extra)
        return len(set(nums))
