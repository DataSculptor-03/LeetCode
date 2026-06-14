class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        l = []

        for i in queries:
            p = 0
            flag = True

            for j in range(len(i)):
                if p < len(pattern) and i[j] == pattern[p]:
                    p += 1
                elif i[j].isupper():
                    flag = False
                    break

            if p != len(pattern):
                flag = False

            l.append(flag)

        return l
