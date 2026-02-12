class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s = []
        sp = text.split()
        for i in range(2, len(sp)):
            if sp[i-2] == first and sp[i-1] == second:
                s.append(sp[i])
        return s
