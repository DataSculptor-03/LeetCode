class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        l=list(s)
        l.sort()
        count=0
        for i in range(1,len(l)-1):
            if l[i-1]<l[i]<l[i+1]:
                count+=nums.count(l[i])
        return count
