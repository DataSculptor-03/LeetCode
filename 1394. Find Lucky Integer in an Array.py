class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l=[]
        s=set(arr)
        for i in s:
            if arr.count(i)==i:
                l.append(i)
        if len(l)>0:
            return max(l)
        else:
            return -1
