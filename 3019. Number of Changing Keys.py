class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        s=s.lower()
        for i in range(0,len(s)-1):
            if(ord(s[i])!=ord(s[i+1])):
                count+=1
        return count
