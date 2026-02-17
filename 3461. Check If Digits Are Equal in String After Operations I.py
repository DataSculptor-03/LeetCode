class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while(len(s)>2):
            arr=""
            for i in range(len(s)-1):
                to=int(s[i])+int(s[i+1])
                rem=to%10
                arr+=str(rem)
            s=arr
        return len(arr)==2 and arr[0]==arr[1]
