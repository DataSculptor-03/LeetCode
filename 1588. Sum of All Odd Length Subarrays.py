class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s=0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)+1):
                if (j-i)%2!=0:
                    s=s+sum(arr[i:j])
        return s
