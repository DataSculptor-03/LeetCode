class Solution(object):
    def primePalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_prime(num):
            if num < 2:
                return False
            if num % 2 == 0:
                return num == 2
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

        def is_palindrome(num):
            s = str(num)
            return s == s[::-1]

        # Special case for small values
        if n <= 2:
            return 2
        if n <= 3:
            return 3
        if n <= 5:
            return 5
        if n <= 7:
            return 7
        if n <= 11:
            return 11

        # Only generate odd-length palindromes after 11
        length = len(str(n))
        while True:
            # Generate odd-length palindromes
            for half in range(10**((length - 1) // 2), 10**((length + 1) // 2)):
                s = str(half)
                pal = int(s + s[-2::-1])  # mirror without last digit
                if pal >= n and is_prime(pal):
                    return pal
            length += 1
