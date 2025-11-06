class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=-1
        for i in range(len(nums)):
            if i%10==nums[i]:
                count=i
                break
        return count
