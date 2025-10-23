class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
            'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
            'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
            'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
        }
        s1=''
        for i in s:
            s1+=str(d[i])
        num=int(s1)
        while k > 0:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            num = total
            k -= 1
        return num
