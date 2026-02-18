class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        l=[]
        cal=0
        for i in nums:
            if i%2==0:
                l.append(i)
        if len(l)==0:
            return 0
        elif len(l)==1:
            return l[0]
        else:
            for i in l:
                cal=cal|i
        return cal
