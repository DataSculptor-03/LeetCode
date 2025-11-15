class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        l=[]
        s=set(arr)
        count=0
        for i in s:
            l.append(arr.count(i))
        for i in l:
            if l.count(i)>1:
                count=1
                break
        if count==1:
            return False
        else:
            return True
