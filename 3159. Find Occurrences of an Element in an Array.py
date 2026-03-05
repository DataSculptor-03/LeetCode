class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        indices = [i for i, num in enumerate(nums) if num == x]
        l = []
        for q in queries:
            if q > len(indices):
                l.append(-1)
            else:
                l.append(indices[q-1])
        return l
