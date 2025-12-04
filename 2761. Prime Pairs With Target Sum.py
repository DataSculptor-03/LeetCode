class Solution(object):
    def findPrimePairs(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        res = []
        for a in range(2, n // 2 + 1):
            b = n - a
            if is_prime[a] and is_prime[b]:
                res.append([a, b])
        
        return res
