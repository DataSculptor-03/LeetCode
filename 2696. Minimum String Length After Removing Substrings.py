class Solution:
    def minLength(self, s: str) -> int:
        s=s.lower()
        while 'ab' in s or 'cd' in s:
            s=s.replace('ab',"")
            s=s.replace('cd',"")
        return len(s)
