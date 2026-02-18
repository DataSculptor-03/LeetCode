class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set(word)
        count=0
        for i in s:
            if i.islower() and i.upper() in s:
                count+=1
        return count
