class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s=""
        l=[]
        for i in nums:
            s+=str(i)
            inte=int(s,2)
            if inte%5==0:
                l.append(True)
            else:
                l.append(False)
        return l
