class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)   
        for i in range(len(s)):
            if s[i].isdigit():
                for j in range(i-1, -1, -1):
                    if s[j].isalpha():
                        s[i] = ""  
                        s[j] = ""   
                        break
        return "".join(s)
