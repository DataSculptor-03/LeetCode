class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(0,len(s)-2):
            s1=s[i:i+3]
            se=set(s1)
            if len(se)==3:
                count+=1
        return count
