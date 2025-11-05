class Solution(object):
    def splitWordsBySeparator(self, words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        l=[]
        for i in range(len(words)):
            sp=words[i].split(separator)
            for s in sp:
                if s:
                    l.append(s)
        return l
