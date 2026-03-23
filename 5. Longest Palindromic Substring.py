class Solution:
    def longestPalindrome(self, s: str) -> str:
        m=0
        ns=""
        for i in range(0,len(s)):
            for j in range(i+1,len(s)+1):
                arr=s[i:j]
                if arr==arr[::-1]:
                    if len(arr)>m:
                        m=len(arr)
                        ns=arr
        return ns
