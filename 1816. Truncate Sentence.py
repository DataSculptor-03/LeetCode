class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a=''
        count=0
        for i in range(len(s)):
            if(count!=k):
                a+=s[i]
                if(s[i]==" "):
                    count+=1
        if(a[len(a)-1]==" "):
            return a[0:len(a)-1]
        else:
            return a[0:len(a)]
