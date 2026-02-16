class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        l = []
        for i in nums:
            bi = bin(i)[2:]
            l.append(str(bi))
        
        m = 0
        for i in l:
            if len(i) >= m:
                m = len(i)
        
        for idx in range(len(l)):
            l[idx] = l[idx].zfill(m)
        
        count = 0
        s = ""
        for i in range(len(l[0])):
            count = 0
            for j in range(len(l)):
                if l[j][i] == '1':
                    count += 1
            if count >= k:
                s += '1'
            else:
                s += '0'
        
        return int(s, 2)
