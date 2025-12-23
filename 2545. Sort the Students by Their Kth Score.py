class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        l=[]
        li=[]
        for i in score:
            l.append(i[k])
        l.sort()
        for i in range(len(l)-1,-1,-1):
            for j in score:
                if l[i] in j:
                    li.append(j)
                    break
        return li
