class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        l=[]
        for i in sentences:
            sp=i.split()
            l.append(len(sp))
        return max(l)
