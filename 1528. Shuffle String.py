class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s1=""
        for i in range(0,len(indices)):
            for j in range(len(indices)):
                if i==indices[j]:
                    s1+=str(s[j])
                    break
        return s1
