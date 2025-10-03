class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        s=set()
        for i in sentence:
            if i not in s:
                s.add(i)
        if len(s)==26:
            return True
        else:
            return False
