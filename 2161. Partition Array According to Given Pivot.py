class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        l1=[]
        l2=[]
        l3=[]
        for i in nums:
            if i<pivot:
                l1.append(i)
            elif i>pivot:
                l3.append(i)
            elif i==pivot:
                l2.append(i)
        l=l1+l2+l3
        return l
