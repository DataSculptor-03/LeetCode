class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        s1=set(allowed)
        for i in words:
            s2=set(i)
            if s2.issubset(s1):
                count+=1
        return count
