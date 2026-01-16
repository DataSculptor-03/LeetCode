class Solution:
    def finalString(self, s: str) -> str:
        s1=""
        for i in range(0,len(s)):
            if s[i]!='i':
                s1+=s[i]
            else:
                s1=s1[::-1]
        return s1
