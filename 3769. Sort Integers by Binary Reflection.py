class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        l=[]
        for i in nums:
            cal=bin(i)[2:]
            r=cal[::-1]
            l.append((int(r,2),i))
        l.sort()
        li=[]
        for _,val in l:
            li.append(val)
        return li
