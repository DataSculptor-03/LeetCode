class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        s = str(num)
        for i in range(len(s) - k + 1):
            cal = int(s[i:i+k])
            if cal != 0 and num % cal == 0:
                count += 1
        return count
