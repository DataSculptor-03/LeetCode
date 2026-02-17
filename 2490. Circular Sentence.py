class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sp = sentence.split(" ")
        for i in range(len(sp)-1):
            if sp[i][-1] != sp[i+1][0]:
                return False
        if sp[-1][-1] != sp[0][0]:
            return False
        return True
