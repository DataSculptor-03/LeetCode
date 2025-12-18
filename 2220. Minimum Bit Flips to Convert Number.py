class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        b1=bin(start)[2:]
        b2=bin(goal)[2:]
        length = max(len(b1), len(b2))
        s1 = b1.zfill(length)   
        s2 = b2.zfill(length)

        count=0
        for i in range(length):
            if s1[i] != s2[i]:
                count += 1
        return count
