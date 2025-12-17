class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        idx=0
        l=[]
        for i in range(0,len(order)):
            for j in range(0,len(friends)):
                if order[i]==friends[j]:
                    l.append(order[i])
        return l
