class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l1=nums[0:n]
        l2=nums[n:len(nums)]
        l=len(nums)
        li=[]
        for i in range(0,l//2):
            li.append(l1[i])
            li.append(l2[i])
        return li
