class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        count=0
        for i in range(2,n-1):
            s=""
            temp=n
            while(temp!=0):
                rem=temp%i
                s+=str(rem)
                temp//=i  
            if s==s[::-1]:
                count=1
            else:
                count=0
                break
        return count==1
