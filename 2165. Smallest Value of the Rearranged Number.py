class Solution:
    def smallestNumber(self, num: int) -> int:
        l = [int(ch) for ch in str(abs(num))]  # Extract digits
        
        if num >= 0:
            l.sort()
            n = ''
            if l[0] == 0: 
                for i in range(len(l)):
                    if l[i] != 0:
                        l[0], l[i] = l[i], l[0]
                        break
            for i in range(len(l)):
                n += str(l[i])
            return int(n)
        
        else:
            l.sort(reverse=True)
            n = ''
            for i in range(len(l)):
                n += str(l[i])
            return -int(n)        
