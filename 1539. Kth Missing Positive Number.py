class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i=1
        mov=0
        l=[]
        while(True):
            if i not in arr:
                l.append(i)
                i+=1
                if len(l)==k:
                    break
            else:
                i+=1
        return l[k-1]
