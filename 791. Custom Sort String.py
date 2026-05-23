class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s1 = ""
        for ch in order:
            count = s.count(ch)
            s1 += ch * count
        for ch in s:
            if ch not in order:
                s1 += ch
        return s1
