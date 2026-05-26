class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        l=[]
        l3=[]
        l4=[]
        l1=[]
        l2=[]
        
        loss_count = {}

        for i in range(len(matches)):
            a,b = matches[i][0], matches[i][1]
            l1.append(a)
            l2.append(b)

            if b in loss_count:
                loss_count[b] += 1
            else:
                loss_count[b] = 1

        s1 = set(l1)
        s2 = set(l2)
        players = s1.union(s2)

        for i in players:
            c = loss_count.get(i, 0)
            if c == 0:
                l3.append(i)
            elif c == 1:
                l4.append(i)

        l3.sort()
        l4.sort()
        li = [l3, l4]
        return li
