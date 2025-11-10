class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s=''
        i=0
        while i < len(word1) and i < len(word2):
            s += word1[i] + word2[i]
            i += 1
        s+=word1[i:]+word2[i:]
        return s
