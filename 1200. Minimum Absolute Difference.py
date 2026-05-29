class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        d = float('inf')
        for i in range(len(arr) - 1):
            d = min(d, arr[i+1] - arr[i])
        res = []
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == d:
                res.append([arr[i], arr[i+1]])
        return res
