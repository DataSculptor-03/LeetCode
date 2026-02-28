class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        rn=0
        n1=0
        l=[]
        for i in range(len(mat)):
            if mat[i].count(1)>n1:
                rn=i
                n1=mat[i].count(1)
        l.append(rn)
        l.append(n1)
        return l
