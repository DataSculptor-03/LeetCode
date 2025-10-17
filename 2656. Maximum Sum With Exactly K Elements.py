class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=0
        cu=0
        for i in range(0,k):
            ma=max(nums)
            s+=ma
            nums.remove(ma)
            cu=ma+1
            nums.append(cu)
        return s
