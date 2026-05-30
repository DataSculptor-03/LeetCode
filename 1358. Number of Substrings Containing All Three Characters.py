class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last = [-1, -1, -1]
        res = 0
        for i, ch in enumerate(s):
            last[ord(ch) - ord('a')] = i
            if -1 not in last:
                res += min(last) + 1   
        return res
