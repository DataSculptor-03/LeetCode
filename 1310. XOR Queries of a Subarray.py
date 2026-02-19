class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        result = []
        for L, R in queries:
            result.append(prefix[R + 1] ^ prefix[L])
        return result
