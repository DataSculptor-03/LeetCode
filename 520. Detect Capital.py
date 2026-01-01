class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up=word.upper()
        lo=word.lower()
        if up==word:
            return True
        elif lo==word:
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
