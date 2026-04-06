class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        def prime(num):
            if num < 2:
                return 0
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return 0
            return 1

        f = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                f.append(i)
                if i != n // i:
                    f.append(n // i)

        for p in [2, 3, 5]:
            if p in f:
                f.remove(p)

        count = 1
        for i in f:
            if prime(i):
                count = 0
                break

        return count == 1
