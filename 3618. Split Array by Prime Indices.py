class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def is_prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            if n % 2 == 0:
                return False
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True

        p = []
        np = []
        
        for i in range(len(nums)):
            if is_prime(i):
                p.append(nums[i])
            else:
                np.append(nums[i])
        
        s1 = sum(p)
        s2 = sum(np)
        return abs(s1 - s2)
