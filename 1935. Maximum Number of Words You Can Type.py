class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        sp=text.split()
        count=0
        for i in sp:
            for j in range(0,len(brokenLetters)):
                if brokenLetters[j] in i:
                    break
            else:
                count+=1
        return count
