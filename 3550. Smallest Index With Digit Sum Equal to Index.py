class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(0,len(nums)):
            s=str(nums[i])
            if len(s)==1:
                if i==nums[i]:
                    l.append(i)
            elif len(s)>1:
                t=0
                n=nums[i]
                while(n!=0):
                    rem=n%10
                    t+=rem
                    n//=10
                if(t==i):
                    l.append(i)
        if l:
            return min(l)
        else:
            return -1
