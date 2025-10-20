class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        l=[]
        l1=[]
        index=0
        for i in arr2:
            c=arr1.count(i)
            for j in range(c):
                l.append(i)
        for i in arr1:
            if i not in arr2:
                l1.append(i)
        l1.sort()
        l2=l+l1
        return l2
