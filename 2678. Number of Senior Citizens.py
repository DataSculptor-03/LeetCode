class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        l=[]
        for i in details:
            if i[11:13]>"60":
                l.append(i[11:13])
        return len(l)
