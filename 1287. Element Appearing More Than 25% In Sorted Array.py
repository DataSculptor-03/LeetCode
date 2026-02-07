class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l=len(arr)//4
        s=set(arr)
        for i in s:
            if arr.count(i)>l:
                return i
