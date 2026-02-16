class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l = []
        for i in range(len(num) - 2):
            sl = num[i:i+3]
            if sl[0] == sl[1] == sl[2]:
                l.append(int(sl))
        if not l:
            return ""  
        return str(max(l)).zfill(3) 
