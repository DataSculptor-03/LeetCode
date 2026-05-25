class Solution:
    def maxPower(self, s: str) -> int:
        l=[]
        for i in range(0,len(s)):
            uni=s[i]
            count=1
            j = i + 1
            while j < len(s) and s[j] == uni:
                count += 1
                j += 1
            l.append(count)
            i = j - 1  
        return max(l)
