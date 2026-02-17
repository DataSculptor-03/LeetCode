class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sp=sentence.split(" ")
        for i in range(len(sp)):
            if len(sp[i])>=len(searchWord):
                for j in range(len(searchWord)):
                    if searchWord[j]!=sp[i][j]:
                        break
                else:
                    return i+1
        return -1
