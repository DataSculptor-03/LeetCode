class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        fractions = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                fractions.append((arr[i] / float(arr[j]), arr[i], arr[j]))
        
        fractions.sort(key=lambda x: x[0])
        return [fractions[k - 1][1], fractions[k - 1][2]]
