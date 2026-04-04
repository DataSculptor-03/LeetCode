class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        to=0
        l1=list(s)
        l2=list(t)
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i]==l2[j]:
                    to+=abs(i-j)
                    break
        return to
