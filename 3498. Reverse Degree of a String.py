class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = 0
        for i in range(len(s)):
            if s[i] == 'a':
                t += 26 * (i + 1)
            elif s[i] == 'b':
                t += 25 * (i + 1)
            elif s[i] == 'c':
                t += 24 * (i + 1)
            elif s[i] == 'd':
                t += 23 * (i + 1)
            elif s[i] == 'e':
                t += 22 * (i + 1)
            elif s[i] == 'f':
                t += 21 * (i + 1)
            elif s[i] == 'g':
                t += 20 * (i + 1)
            elif s[i] == 'h':
                t += 19 * (i + 1)
            elif s[i] == 'i':
                t += 18 * (i + 1)
            elif s[i] == 'j':
                t += 17 * (i + 1)
            elif s[i] == 'k':
                t += 16 * (i + 1)
            elif s[i] == 'l':
                t += 15 * (i + 1)
            elif s[i] == 'm':
                t += 14 * (i + 1)
            elif s[i] == 'n':
                t += 13 * (i + 1)
            elif s[i] == 'o':
                t += 12 * (i + 1)
            elif s[i] == 'p':
                t += 11 * (i + 1)
            elif s[i] == 'q':
                t += 10 * (i + 1)
            elif s[i] == 'r':
                t += 9 * (i + 1)
            elif s[i] == 's':
                t += 8 * (i + 1)
            elif s[i] == 't':
                t += 7 * (i + 1)
            elif s[i] == 'u':
                t += 6 * (i + 1)
            elif s[i] == 'v':
                t += 5 * (i + 1)
            elif s[i] == 'w':
                t += 4 * (i + 1)
            elif s[i] == 'x':
                t += 3 * (i + 1)
            elif s[i] == 'y':
                t += 2 * (i + 1)
            elif s[i] == 'z':
                t += 1 * (i + 1)
        return t
