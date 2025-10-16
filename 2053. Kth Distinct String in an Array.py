class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        l=[]
        for i in arr:
            if arr.count(i)==1:
                l.append(i)
        if k<=len(l):
            return (l[k-1])
        else:
            return ""
