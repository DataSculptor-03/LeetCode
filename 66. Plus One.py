class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=''
        l=[]
        c=0
        for i in digits:
            s+=str(i)
        c=(int)(s)+1
        s1=str(c)
        for i in s1:
            l.append(int(i))
        return l
