class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p=[]
        n=[]
        t=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        for i in range(0,len(p)):
            t.append(p[i])
            t.append(n[i])
        return t
