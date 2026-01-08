class Solution:
    def countSegments(self, s: str) -> int:
        if s=="":
            return 0
        else:
            s1=s.split()
            return len(s1)
