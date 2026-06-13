class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in range(0,len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        o.sort()
        o.reverse()
        e.sort()
        res=[]
        ei=oi=0
        for i in range(len(nums)):
            if i%2==0:
                res.append(e[ei])
                ei+=1
            else:
                res.append(o[oi])
                oi+=1
        return res
