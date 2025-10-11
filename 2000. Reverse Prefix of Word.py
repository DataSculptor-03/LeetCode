class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        stop=-1
        new=''
        for i in range(len(word)):
            if word[i]==ch:
                stop=i
                break
        if stop==-1:
            return word
        for j in range(stop,-1,-1):
            new+=word[j]
        for j in range(stop+1,len(word)):
            new+=word[j]
        return new
