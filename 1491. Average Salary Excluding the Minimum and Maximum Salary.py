class Solution:
    def average(self, salary: List[int]) -> float:
        s=set(salary)
        l=list(s)
        ma=max(l)
        mi=min(l)
        l.remove(ma)
        l.remove(mi)
        return sum(l)/len(l)
