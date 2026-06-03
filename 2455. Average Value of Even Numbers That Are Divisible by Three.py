class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            if i%2==0 and i%3==0:
                l.append(i)
        if len(l)==0:
            return 0
        else:
            t=sum(l)
            return t//len(l)
