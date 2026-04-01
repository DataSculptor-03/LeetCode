class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        s1 = list(s1)
        n = len(s1)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                s1[i], s1[j] = s1[j], s1[i]
                if ''.join(s1) == s2:
                    return True
                s1[i], s1[j] = s1[j], s1[i]
        return False
