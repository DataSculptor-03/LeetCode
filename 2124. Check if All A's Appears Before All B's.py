class Solution:
    def checkString(self, s: str) -> bool:
        count=1
        for i in range(len(s)):
            if s[i]=='b':
                s1=s[i:len(s)]
                if 'a' in s1:
                    count=0
        return count==1
