class Solution:
    def replaceDigits(self, s: str) -> str:
        s1=""
        for i in range(len(s)):
            if s[i].isalpha():
                s1+=str(s[i])
            else:
                cal=ord(s[i-1])
                t=cal+int(s[i])
                c=chr(t)
                s1+=c
        return s1
